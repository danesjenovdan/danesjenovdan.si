import json
import re

import requests
from wagtail.embeds.exceptions import EmbedNotFoundException
from wagtail.embeds.finders.base import EmbedFinder

rtv_urls = [
    r"^https?://365\.rtvslo\.si/embed/.+$",
    r"^https?://365\.rtvslo\.si/arhiv/.+$",
]


class RtvEmbedFinder(EmbedFinder):
    _patterns = None

    def __init__(self):
        self._patterns = []

        for url in rtv_urls:
            self._patterns.append(re.compile(url))

    def accept(self, url):
        for pattern in self._patterns:
            if re.match(pattern, url):
                return True
        return False

    def _get_embed_url(self, url):
        if "/embed/" in url:
            return url, None

        try:
            r = requests.get(url, headers={"User-agent": "Mozilla/5.0"}, timeout=10)
            r.raise_for_status()
            html = r.text
        except requests.RequestException:
            raise EmbedNotFoundException

        # Extract embed URL from JSON-LD script tag
        match = re.search(
            r'<script type="application/ld\+json">(.+?)</script>',
            html,
            re.DOTALL,
        )
        if match:
            try:
                data = json.loads(match.group(1))
            except json.JSONDecodeError:
                data = {}

            if "embedUrl" in data:
                embed_url = data["embedUrl"]
                embed_data = {}
                if "name" in data:
                    embed_data["title"] = data["name"]
                if "thumbnailUrl" in data:
                    thumbnails = data["thumbnailUrl"]
                    if isinstance(thumbnails, list) and thumbnails:
                        embed_data["thumbnail_url"] = thumbnails[0]
                    elif isinstance(thumbnails, str):
                        embed_data["thumbnail_url"] = thumbnails
                return embed_url, embed_data

        # Fallback: extract ID from URL
        url_path = url.split("?")[0]
        url_parts = url_path.rstrip("/").split("/")
        url_id = url_parts[-1]
        if url_id.isdigit():
            embed_url = f"https://365.rtvslo.si/embed/{url_id}"
            return embed_url, None

        raise EmbedNotFoundException

    def _get_embed_data(self, url):
        try:
            r = requests.get(url, headers={"User-agent": "Mozilla/5.0"}, timeout=10)
            r.raise_for_status()
            html = r.text
        except requests.RequestException:
            return {}

        # Find line that starts with "let data = "
        match = re.search(r"let data = ({.+?});", html, re.DOTALL)
        if match:
            try:
                data = json.loads(match.group(1))
            except json.JSONDecodeError:
                data = {}

            embed_data = {}
            data_data = data.get("data", {})
            if "title" in data_data:
                embed_data["title"] = data_data["title"]
            thumbnail = data_data.get("images", {}).get("orig", "")
            if thumbnail:
                embed_data["thumbnail_url"] = thumbnail
            elif "thumbnail_sec" in data_data:
                embed_data["thumbnail_url"] = data_data["thumbnail_sec"]
            return embed_data

        return {}

    def find_embed(self, url, max_width=None, max_height=None):
        embed_url, embed_data = self._get_embed_url(url)
        if embed_url is None:
            raise EmbedNotFoundException
        if embed_data is None:
            embed_data = self._get_embed_data(embed_url)

        print(embed_url, embed_data)

        return {
            "title": embed_data.get("title", ""),
            "author_name": "Multimedijski center RTV Slovenija",
            "provider_name": "RTVSLO.si",
            "type": "video",
            "thumbnail_url": embed_data.get("thumbnail_url", ""),
            "width": "",
            "height": "",
            "html": f'<iframe class="custom-video-embed" src="{embed_url}"></iframe>',
        }


embed_finder_class = RtvEmbedFinder
