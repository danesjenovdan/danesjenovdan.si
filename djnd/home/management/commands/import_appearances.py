import traceback

import requests
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from home.models import Activity, ActivityCategory
from wagtail.models import Locale

from ._save_image import save_image


class Command(BaseCommand):
    help = "Import appearances from old site"

    def _get_category(self):
        locale = Locale.get_default()
        category, created = ActivityCategory.objects.get_or_create(
            name="V medijih", locale=locale
        )
        return category

    def _save_appearance_activity(self, appearance, category):
        image = save_image(self, appearance["image"], prefix="appearance-")
        locale = Locale.get_default()

        try:
            old_activity = Activity.objects.get(
                title=appearance["title"],
                link=appearance["url"],
                date=appearance["date"],
                locale=locale,
            )
            return old_activity
        except Activity.DoesNotExist:
            date = appearance["date"]
            new_activity = Activity(
                locale=locale,
                title=appearance["title"],
                link=appearance["url"],
                description=appearance["desc"],
                note=appearance["publisher"],
                date=date,
                image=image,
            )
            new_activity.save()
            new_activity.category.add(category)
            new_activity.save()
            return new_activity

    def handle(self, *args, **options):
        self.stdout.write("")
        self.stdout.write(self.style.SUCCESS("Start importing appearances..."))

        url = "https://djnapi.djnd.si/djnd.si/clips/?lang=sl&ordering=date&size=50"

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

                for appearance in data:
                    index += 1
                    self.stdout.write(
                        f"Importing appearances {index}/{count}...", ending="\r"
                    )
                    with transaction.atomic():
                        activity = self._save_appearance_activity(appearance, category)

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
