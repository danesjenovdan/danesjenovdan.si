from django.core.paginator import InvalidPage, Page, Paginator
from django.utils.functional import cached_property
from wagtail.models import Locale

from .models.snippets import Activity, ActivityProject

#
# FILTERING HELPERS
#


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

    activities = filtered_activities.order_by("-date", "pk")

    return activities, form


#
# CUSTOM PAGINATION WITH LIMIT/OFFSET
#


class LimitOffsetPaginatorStub:
    """
    Paginator stub that doesn't actually paginate, but just holds info needed
    by LimitOffsetPage.
    """

    def __init__(self, object_list):
        self.object_list = object_list

    @cached_property
    def count(self):
        """Return the total number of objects, across all pages."""
        return Paginator.count.real_func(self)


class LimitOffsetPage(Page):
    """
    Based on Django's Page class, but with limit/offset pagination.
    """

    def __init__(self, object_list, limit, offset, paginator):
        super().__init__(object_list, -1, paginator)
        self.limit = limit
        self.offset = offset

    def __repr__(self):
        return f"<LimitOffsetPage limit={self.limit} offset={self.offset}>"

    def __len__(self):
        return len(self.object_list)

    def has_next(self):
        return self.offset + self.limit < self.paginator.count

    def has_previous(self):
        return self.offset > 0

    def next_page_offset(self):
        return self.offset + self.limit

    def previous_page_offset(self):
        return self.offset - self.limit

    def next_page_number(self):
        raise InvalidPage(
            "LimitOffsetPage is not page-based, call `next_page_offset` instead"
        )

    def previous_page_number(self):
        raise InvalidPage(
            "LimitOffsetPage is not page-based, call `previous_page_offset` instead"
        )

    def start_index(self):
        # Special case, return zero if no items.
        if self.paginator.count == 0:
            return 0
        return self.offset + 1

    def end_index(self):
        if self.has_next():
            return self.offset + self.limit
        return self.paginator.count


def paginate_activities(activities, limit=12, offset=0):
    paginator = LimitOffsetPaginatorStub(activities)
    paged_object_list = activities[offset : offset + limit]
    return LimitOffsetPage(paged_object_list, limit, offset, paginator)
