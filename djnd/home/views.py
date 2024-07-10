from django.views.generic import ListView
from home.forms import OurWorkForm
from home.models import Activity, ActivityCategory
from wagtail.models import Locale


class ActivityView(ListView):
    model = Activity
    template_name = "home/activities.html"
    context_object_name = "activities"
    paginate_by = 7
    ordering = ["-date"]

    def get_queryset(self):
        slovenian_locale = Locale.objects.get(language_code="sl")

        filtered_activities = Activity.objects.filter(locale=slovenian_locale)

        form = OurWorkForm(self.request.GET, locale=slovenian_locale)
        filtered_activities = form.filter_activities(filtered_activities)

        # get only activities that have english translation
        if self.request.LANGUAGE_CODE == "en":
            locale = Locale.get_active()
            en_activities_translation_keys = Activity.objects.filter(
                locale=locale
            ).values_list("translation_key", flat=True)
            filtered_activities = filtered_activities.filter(
                translation_key__in=en_activities_translation_keys
            )

        activities = filtered_activities.order_by("-date")

        return activities


class ActivityHomepageView(ListView):
    model = Activity
    template_name = "home/activities-homepage.html"
    context_object_name = "activities"
    paginate_by = 7
    ordering = ["-date"]

    def get_queryset(self):
        slovenian_locale = Locale.objects.get(language_code="sl")

        filtered_activities = Activity.objects.filter(locale=slovenian_locale)

        # homepage filtering
        filter = self.request.GET.get("filter", "")
        if filter == "promoted":
            filtered_activities = Activity.objects.filter(
                locale=slovenian_locale, promoted=True
            )
        elif filter == "newsletter":
            newsletter_category = ActivityCategory.objects.get(name="Občasnik")
            filtered_activities = Activity.objects.filter(
                locale=slovenian_locale, category=newsletter_category
            )

        # get only activities that have english translation
        if self.request.LANGUAGE_CODE == "en":
            locale = Locale.get_active()
            en_activities_translation_keys = Activity.objects.filter(
                locale=locale
            ).values_list("translation_key", flat=True)
            filtered_activities = filtered_activities.filter(
                translation_key__in=en_activities_translation_keys
            )

        activities = filtered_activities.order_by("-date")

        return activities
