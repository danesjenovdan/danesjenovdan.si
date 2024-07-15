from wagtail.models import Locale

from .models.snippets import Activity, ActivityProject


def _filter_activities_homepage(request, activities):
    filter = request.GET.get("filter", "")

    if filter == "promoted":
        activities = activities.filter(promoted=True)

    if filter == "newsletter":
        try:
            newsletter_project = ActivityProject.objects.get(name="Občasnik")
            activities = activities.filter(project=newsletter_project)
        except ActivityProject.DoesNotExist:
            return activities.none()

    return activities.distinct()


def get_filtered_activities(request, for_homepage=False):
    # get all slovenian activities (for filtering purposes)
    sl_locale = Locale.objects.get(language_code="sl")
    sl_activities = Activity.objects.filter(locale=sl_locale)

    # import here to avoid circular imports
    from .forms import OurWorkForm

    if not for_homepage:
        # filter the activities via the form using slovenian locale because
        # all activities have foreign keys to the slovenian locale categories
        form = OurWorkForm(request.GET, locale=sl_locale)
        filtered_activities = form.filter_activities(sl_activities)
    else:
        # homepage filtering
        form = None
        filtered_activities = _filter_activities_homepage(request, sl_activities)

    # if the active locale is not slovenian, we need to get the translations
    # via the translation key
    active_locale = Locale.get_active()
    if active_locale.pk != sl_locale.pk:
        translation_keys = filtered_activities.values_list("translation_key", flat=True)
        filtered_activities = Activity.objects.filter(
            locale=active_locale, translation_key__in=translation_keys
        )

    activities = filtered_activities.order_by("-date")

    return activities, form
