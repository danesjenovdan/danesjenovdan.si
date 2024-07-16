from django.views.generic import TemplateView
from wagtail.models import Locale

from .models.pages import NewsletterListPage, NewsletterPage
from .pagination import get_filtered_activities, paginate_limit_offset


def _activity_pagination_context(request, for_homepage=False):
    offset = int(request.GET.get("offset", 0))

    activities, _ = get_filtered_activities(request, for_homepage=for_homepage)
    activities = paginate_limit_offset(activities, limit=12, offset=offset)

    return {
        "page_obj": activities,
        "activities": activities.object_list,
    }


class ActivityView(TemplateView):
    template_name = "home/activities.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(_activity_pagination_context(self.request))
        return context


class ActivityHomepageView(TemplateView):
    template_name = "home/activities-homepage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(_activity_pagination_context(self.request, for_homepage=True))
        return context


class NewsletterListView(TemplateView):
    template_name = "home/newsletters.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        parent = int(self.request.GET.get("parent", 0))
        parent_page = NewsletterListPage.objects.filter(pk=parent).first()

        offset = int(self.request.GET.get("offset", 0))
        locale = Locale.get_active()

        newsletters = (
            NewsletterPage.objects.child_of(parent_page)
            .filter(locale=locale)
            .live()
            .order_by("-published_at", "pk")
        )
        newsletters = paginate_limit_offset(newsletters, limit=12, offset=offset)

        context["page_obj"] = newsletters
        context["newsletters"] = newsletters.object_list

        return context
