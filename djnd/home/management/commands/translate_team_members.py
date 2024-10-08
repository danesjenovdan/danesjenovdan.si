import traceback

import requests
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from wagtail.models import Locale

from home.models import TeamMember, TeamMemberCategory


class Command(BaseCommand):
    help = "Make translations of all team member snippets"

    def handle(self, *args, **options):
        self.stdout.write("")
        self.stdout.write(self.style.SUCCESS("Start..."))

        language_code = "en"

        sl_locale = Locale.get_default()
        trans_locale = Locale.objects.get(language_code=language_code)

        team_members = TeamMember.objects.filter(locale=sl_locale)
        team_member_categories = TeamMemberCategory.objects.filter(locale=sl_locale)

        for team_member in team_members:
            try:
                trans_tm = team_member.get_translation(trans_locale)
            except TeamMember.DoesNotExist:
                trans_tm = team_member.copy_for_translation(trans_locale)
                trans_tm.save()

        for team_member_category in team_member_categories:
            try:
                trans_tmc = team_member_category.get_translation(trans_locale)
            except TeamMemberCategory.DoesNotExist:
                trans_tmc = team_member_category.copy_for_translation(trans_locale)
                trans_tmc.save()

        self.stdout.write(self.style.SUCCESS("Done!"))
        self.stdout.write("")
