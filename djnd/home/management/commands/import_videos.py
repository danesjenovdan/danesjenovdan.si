import traceback

import requests
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from home.models import Activity, ActivityCategory
from wagtail.models import Locale

from ._save_image import save_image


class Command(BaseCommand):
    help = "Import videos from old site"

    def _get_category(self, language_code=None):
        locale = Locale.get_default()
        category, created = ActivityCategory.objects.get_or_create(
            name="Video", locale=locale
        )
        if language_code:
            trans_locale = Locale.objects.get(language_code=language_code)
            try:
                trans_cat = category.get_translation(trans_locale)
            except ActivityCategory.DoesNotExist:
                trans_cat = category.copy_for_translation(trans_locale)
                trans_cat.name = "Video"
                trans_cat.save()
        return category

    def _save_video_activity(self, video, category):
        image = save_image(self, video["image"], tag="video")
        locale = Locale.get_default()

        try:
            old_activity = Activity.objects.get(
                title=video["title"],
                link=video["url"],
                date=video["date"],
                locale=locale,
            )
            return old_activity
        except Activity.DoesNotExist:
            date = video["date"]
            new_activity = Activity(
                locale=locale,
                title=video["title"],
                link=video["url"],
                description=video["desc"],
                date=date,
                image=image,
            )
            new_activity.save()
            new_activity.category.add(category)
            new_activity.save()
            return new_activity

    def _save_video_activity_en(self, video, category):
        locale = Locale.get_default()
        trans_locale = Locale.objects.get(language_code="en")

        old_activity = Activity.objects.get(
            locale=locale,
            link=video["url"],
            date=video["date"],
            category=category,
        )
        try:
            new_activity = old_activity.get_translation(trans_locale)
        except Activity.DoesNotExist:
            new_activity = old_activity.copy_for_translation(trans_locale)
            new_activity.title = video["title"]
            new_activity.description = video["desc"]
            new_activity.save()

        return new_activity

    def handle(self, *args, **options):
        self.stdout.write("")
        self.stdout.write(self.style.SUCCESS("Start importing videos..."))

        url = "https://djnapi.djnd.si/djnd.si/videos/?lang=sl&ordering=date&size=50"
        url_en = (
            "https://djnapi.djnd.si/djnd.si/videos/?lang=en&ordering=date&size=50"
        )

        try:
            category = self._get_category()
            index = 0

            while url is not None:
                response = requests.get(url)
                response.raise_for_status()
                res_json = response.json()
                count = res_json["count"]
                data = res_json["results"]
                next_url = res_json["next"]

                for video in data:
                    index += 1
                    self.stdout.write(
                        f"Importing video (sl) {index}/{count}...", ending="\r"
                    )
                    with transaction.atomic():
                        activity = self._save_video_activity(video, category)

                url = next_url

            self.stdout.write("")

            category_en = self._get_category("en")
            index = 0

            while url_en is not None:
                response = requests.get(url_en)
                response.raise_for_status()
                res_json = response.json()
                count = res_json["count"]
                data = res_json["results"]
                next_url = res_json["next"]

                for video in data:
                    index += 1
                    self.stdout.write(
                        f"Importing video (en) {index}/{count}...", ending="\r"
                    )
                    with transaction.atomic():
                        activity = self._save_video_activity_en(video, category)

                url_en = next_url

        except requests.RequestException as e:
            self.stdout.write("")
            raise CommandError(f"Failed to fetch data: {e}")
        except Exception as e:
            self.stdout.write("")
            traceback.print_exc()
            raise CommandError(f"Failed to import data: {e}")

        self.stdout.write(self.style.SUCCESS("Done!"))
        self.stdout.write("")