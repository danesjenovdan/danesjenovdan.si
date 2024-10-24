import traceback
from datetime import datetime

import requests
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from django.utils.formats import date_format
from django.utils.text import slugify
from wagtail.blocks.stream_block import StreamValue
from wagtail.models import Locale, Page, Site

from home.models import Activity, ActivityCategory, BlogListingPage, BlogPage

from ._save_image import get_image, save_image


class Command(BaseCommand):
    help = "Import agruments from old site"

    def _get_category(self):
        locale = Locale.get_default()
        category, created = ActivityCategory.objects.get_or_create(
            name="Agrument", locale=locale
        )
        return category

    def _get_parent_page(self):
        locale = Locale.get_default()
        site = Site.objects.get(is_default_site=True)
        root_page = site.root_page.get_translation(locale)
        try:
            sub_page = root_page.get_children().get(slug="agrument")
        except Page.DoesNotExist:
            sub_page = root_page.add_child(instance=BlogListingPage(title="Agrument"))
        return sub_page

    def _fix_agrument_page_date(self, agrument, parent_page, category):
        image = get_image(self, agrument["image_url"], tag="agrument")

        try:
            old_page = BlogPage.objects.child_of(parent_page).get(
                title=agrument["title"],
                short_description=agrument["description"],
            )

            date = agrument["datetime"].split("T")[0]
            old_page.published_at = date

            raw_html = f""

            if image:
                alt_text = agrument["image_alt_text"] or image.title
                raw_html += f'<embed alt="{alt_text}" embedtype="image" format="fullwidth" id="{image.id}"/>'

                image_source = agrument["image_source"]
                image_source_url = agrument["image_source_url"]

                if image_source and image_source_url:
                    raw_html += f'<p><i>Slika: <a href="{image_source_url}" target="_blank">{image_source}</a></i></p>'
                elif image_source:
                    raw_html += f"<p><i>Slika: {image_source}</i></p>"

            raw_html += (
                agrument["content_html"]
                if agrument["content_html"].startswith("<p>")
                else f"<p>{agrument['content_html']}</p>"
            )

            if "<br>" in raw_html:
                raw_html = raw_html.replace("<br>", "<br />")

            old_page.modules = StreamValue(
                old_page.modules.stream_block,
                is_lazy=True,
                stream_data=[
                    {
                        "type": "text_content_block",
                        "value": {
                            "text": raw_html,
                            "title": "",
                            "button": [],
                        },
                    }
                ],
            )

            old_page.save_revision().publish()
            return old_page
        except BlogPage.DoesNotExist:
            raise Exception("Page not found")
        except BlogPage.MultipleObjectsReturned:
            raise Exception("Multiple pages found")

    def _save_agrument_page(self, agrument, parent_page, category):
        image = save_image(self, agrument["image_url"], tag="agrument")

        try:
            old_page = BlogPage.objects.child_of(parent_page).get(
                title=agrument["title"],
                short_description=agrument["description"],
            )
            return old_page
        except BlogPage.DoesNotExist:
            slug = slugify(agrument["title"])
            if slug == "" and agrument["datetime"] == "2019-03-21T00:00:00.000Z":
                slug = slugify("Emodžiji")
            while parent_page.get_children().filter(slug=slug).exists():
                slug += "-2"

            new_page = BlogPage(
                color="mint",
                title=agrument["title"],
                slug=slug,
                short_description=agrument["description"],
                first_published_at=agrument["datetime"],
            )

            parent_page.add_child(instance=new_page)
            new_page.save_revision()

            date = agrument["datetime"].split("T")[0]
            formatted_date = date_format(datetime.strptime(date, "%Y-%m-%d"), "j. F Y")
            raw_html = f"<p><b>{formatted_date}</b></p>"

            if image:
                alt_text = agrument["image_alt_text"] or image.title
                raw_html += f'<embed alt="{alt_text}" embedtype="image" format="fullwidth" id="{image.id}"/>'

                image_source = agrument["image_source"]
                image_source_url = agrument["image_source_url"]

                if image_source and image_source_url:
                    raw_html += f'<p><i>Slika: <a href="{image_source_url}" target="_blank">{image_source}</a></i></p>'
                elif image_source:
                    raw_html += f"<p><i>Slika: {image_source}</i></p>"

            raw_html += (
                agrument["content_html"]
                if agrument["content_html"].startswith("<p>")
                else f"<p>{agrument['content_html']}</p>"
            )

            if "<br>" in raw_html:
                raw_html = raw_html.replace("<br>", "<br />")

            new_page.modules = StreamValue(
                new_page.modules.stream_block,
                is_lazy=True,
                stream_data=[
                    {
                        "type": "text_content_block",
                        "value": {
                            "text": raw_html,
                            "title": "",
                            "button": [],
                        },
                    }
                ],
            )
            new_page.thumbnail = image
            new_page.category.add(category)
            new_page.save_revision().publish()
            return new_page

    def _save_agrument_activity(self, agrument, new_page, category):
        image = save_image(self, agrument["image_url"], tag="agrument")
        locale = Locale.get_default()

        date = agrument["datetime"].split("T")[0]
        try:
            old_activity = Activity.objects.get(
                title=agrument["title"],
                date=date,
                locale=locale,
            )
            return old_activity
        except Activity.DoesNotExist:
            new_activity = Activity(
                locale=locale,
                title=agrument["title"],
                page=new_page,
                description=agrument["description"],
                date=date,
                image=image,
            )
            new_activity.save()
            new_activity.category.add(category)
            new_activity.save()
            return new_activity

    def handle(self, *args, **options):
        self.stdout.write("")
        self.stdout.write(self.style.SUCCESS("Start importing agruments..."))

        url = "https://agrument.danesjenovdan.si/api/v2/posts?limit=50&offset=0&sort=timestamp"
        index = 0

        try:
            category = self._get_category()
            parent_page = self._get_parent_page()

            while url is not None:
                response = requests.get(url)
                response.raise_for_status()
                res_json = response.json()
                count = res_json["count"]
                data = res_json["data"]
                next_url = res_json["links"]["next"]

                for agrument in data:
                    index += 1
                    self.stdout.write(
                        f"Importing agrument {index}/{count}...", ending="\r"
                    )
                    with transaction.atomic():
                        page = self._fix_agrument_page_date(
                            agrument, parent_page, category
                        )
                        # page = self._save_agrument_page(agrument, parent_page, category)
                        # activity = self._save_agrument_activity(
                        #     agrument, page, category
                        # )

                url = next_url

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
