import traceback
from html import escape as html_escape

import requests
from django.core.management.base import BaseCommand, CommandError
from wagtail.blocks.stream_block import StreamValue

from home.models.snippets import SocialMediaActivity

BSKY_API_BASE_URL = "https://bsky.social"
USER_HANDLE = "danesjenovdan.si"


class Command(BaseCommand):
    help = "Get new posts from Bluesky API"

    def _resolve_handle_to_did(self, handle):
        url = f"{BSKY_API_BASE_URL}/xrpc/com.atproto.identity.resolveHandle"
        params = {"handle": handle}
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        res_json = response.json()
        return res_json["did"]

    def _fetch_user_posts(self, did):
        url = f"{BSKY_API_BASE_URL}/xrpc/com.atproto.repo.listRecords"
        params = {"repo": did, "collection": "app.bsky.feed.post", "limit": 25}
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        res_json = response.json()
        reverse_records = list(reversed(res_json["records"]))
        return reverse_records

    def _insert_links(self, text, facets):
        bstr = text.encode("utf-8")
        sorted_facets = sorted(facets, key=lambda f: f["index"]["byteStart"])
        cursor = 0

        html = ""

        for facet in sorted_facets:
            for feature in facet["features"]:
                if feature["$type"] == "app.bsky.richtext.facet#link":
                    start = facet["index"]["byteStart"] - cursor
                    end = facet["index"]["byteEnd"] - cursor
                    link_text = html_escape(bstr[start:end].decode("utf-8"))
                    link_url = feature["uri"]
                    html += html_escape(bstr[:start].decode("utf-8"))
                    html += f'<a href="{link_url}">{link_text}</a>'
                    bstr = bstr[end:]
                    cursor += end

        html += html_escape(bstr.decode("utf-8"))

        return html

    def _insert_paragraphs_and_breaks(self, text):
        paragraphs = text.split("\n\n")
        html = "".join(f"<p>{p}</p>" for p in paragraphs)
        html = html.replace("\n", "<br />")
        return html

    def _append_embeds(self, html, embed, did, id):
        if embed.get("$type") == "app.bsky.embed.images":
            for image in embed.get("images", []):
                ref = image["image"]["ref"]["$link"]
                image_url = f"https://cdn.bsky.app/img/feed_fullsize/plain/{did}/{ref}"
                width = image["aspectRatio"]["width"]
                height = image["aspectRatio"]["height"]
                alt = html_escape(image.get("alt", ""), quote=True)
                html += f'<p><img src="{image_url}" alt="{alt}" width="{width}" height="{height}" /></p>'

        if embed.get("$type") == "app.bsky.embed.video":
            ref = embed["video"]["ref"]["$link"]
            # poster_url = f"https://video.bsky.app/watch/{did}/{ref}/thumbnail.jpg"
            width = embed["aspectRatio"]["width"]
            height = embed["aspectRatio"]["height"]
            post_url = f"https://bsky.app/profile/{USER_HANDLE}/post/{id}"
            html += f'<p><a href="{post_url}">Video</a></p>'

        return html

    def _text_to_html(self, did, id, text, facets, embed):
        html = self._insert_links(text, facets)
        html = self._insert_paragraphs_and_breaks(html)
        html = self._append_embeds(html, embed, did, id)
        html += f'<p><a href="https://bsky.app/profile/{USER_HANDLE}/post/{id}">Poglej objavo na Bluesky</a></p>'
        return html

    def _save_post(self, did, id, post):
        created_at = post["value"]["createdAt"]
        text = post["value"].get("text", "")
        facets = post["value"].get("facets", [])
        embed = post["value"].get("embed", {})
        reply = post["value"].get("reply", {})

        if reply:
            parent_id = reply["parent"]["uri"].split("/")[-1]
            parent_obj = SocialMediaActivity.objects.filter(
                uid__contains=parent_id
            ).first()

            if not parent_obj:
                self.stdout.write(f"Parent post {parent_id} not found for reply {id}")
                return

            raw_html = self._text_to_html(did, id, text, facets, embed)

            parent_obj.raw_html.append(
                ("raw_html", raw_html),
            )
            parent_obj.updated_at = created_at
            parent_obj.uid += f" >> {id}"
            parent_obj.save()

            self.stdout.write(f"Saved reply {id} to parent post {parent_id}")
        else:
            raw_html = self._text_to_html(did, id, text, facets, embed)

            new_obj = SocialMediaActivity(
                uid=id,
                post_url=f"https://bsky.app/profile/{USER_HANDLE}/post/{id}",
                created_at=created_at,
                updated_at=created_at,
            )

            new_obj.raw_html = StreamValue(
                new_obj.raw_html.stream_block,
                stream_data=[
                    ("raw_html", raw_html),
                ],
            )

            new_obj.save()
            self.stdout.write(f"Saved post {id}")

    def handle(self, *args, **options):
        self.stdout.write("")
        self.stdout.write(self.style.SUCCESS("Checking Bluesky API..."))

        try:
            did = self._resolve_handle_to_did(USER_HANDLE)
            self.stdout.write(f"Resolved '{USER_HANDLE}' to '{did}'")

            posts = self._fetch_user_posts(did)
            self.stdout.write(f"Fetched {len(posts)} posts from '{USER_HANDLE}'")

            for post in posts:
                id = post["uri"].split("/")[-1]

                if SocialMediaActivity.objects.filter(uid__contains=id).exists():
                    self.stdout.write(f"Post {id} already exists, skipping")
                    continue

                self._save_post(did, id, post)

            self.stdout.write("")

        except requests.RequestException as e:
            self.stdout.write("")
            raise CommandError(f"Failed to fetch data: {e}")
        except Exception as e:
            self.stdout.write("")
            traceback.print_exc()
            raise CommandError(f"Failed to import data: {e}")

        self.stdout.write(self.style.SUCCESS("Done!"))
        self.stdout.write("")
