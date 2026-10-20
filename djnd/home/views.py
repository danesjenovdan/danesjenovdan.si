import datetime

from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView, View
from wagtail.models import Locale, Page, Site

from .models.pages import BlogListingPage, BlogPage, NewsletterListPage, NewsletterPage
from .models.snippets import Activity
from .pagination import get_filtered_activities, paginate_limit_offset


def _activity_pagination_context(request, for_homepage=False):
    offset = int(request.GET.get("offset", 0))

    activities, _ = get_filtered_activities(request, for_homepage=for_homepage)
    activities = paginate_limit_offset(activities, limit=18, offset=offset)

    return {
        "page_obj": activities,
        "activities": activities.object_list,
    }


class ActivityView(TemplateView):
    template_name = "home/activities.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            _activity_pagination_context(
                self.request,
            )
        )
        return context


class ActivityHomepageView(TemplateView):
    template_name = "home/activities-homepage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            _activity_pagination_context(
                self.request,
                for_homepage=True,
            )
        )
        return context


def _subpage_pagination_context(request, context_name, ParentPageModel, SubPageModel):
    parent = int(request.GET.get("parent", 0))
    parent_page = ParentPageModel.objects.filter(pk=parent).first()

    if not parent_page:
        raise Http404(f"Parent page with id {parent} not found.")

    offset = int(request.GET.get("offset", 0))
    locale = Locale.get_active()

    newsletters = (
        SubPageModel.objects.child_of(parent_page)
        .filter(locale=locale)
        .live()
        .order_by("-published_at", "-first_published_at", "pk")
    )
    newsletters = paginate_limit_offset(newsletters, limit=18, offset=offset)

    return {
        "page_obj": newsletters,
        context_name: newsletters.object_list,
    }


class NewsletterListView(TemplateView):
    template_name = "home/newsletters.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            _subpage_pagination_context(
                self.request,
                "newsletters",
                NewsletterListPage,
                NewsletterPage,
            )
        )
        return context


class BlogListView(TemplateView):
    template_name = "home/blogs.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            _subpage_pagination_context(
                self.request,
                "blogs",
                BlogListingPage,
                BlogPage,
            )
        )
        return context


class RandomView(View):
    def get(self, request):
        sl_locale = Locale.objects.get(language_code="sl")
        sl_activities = Activity.objects.filter(locale=sl_locale, page__isnull=False)

        if sl_activities.count() == 0:
            return redirect("/")

        random_activity = sl_activities.order_by("?").first()

        return redirect(random_activity.page.get_url())


# ------------


class AgrumentByDateRedirectView(View):
    def get(self, request, day, month, year):
        date = datetime.date(int(year), int(month), int(day))

        locale = Locale.objects.get(language_code="sl")
        site = Site.objects.get(is_default_site=True)
        root_page = site.root_page.get_translation(locale)
        page = root_page.get_children().filter(slug="agrument").first()

        if page is None:
            raise Http404

        blog = (
            BlogPage.objects.child_of(page)
            .filter(locale=locale, published_at=date)
            .live()
            .order_by("-first_published_at", "pk")
            .first()
        )

        if blog is None:
            raise Http404

        return redirect(blog.get_url(), permanent=True)


ROBOTS_TXT_CONTENT = """

User-agent: *
Disallow: /admin/
Disallow: /django-admin/

Sitemap: https://danesjenovdan.si/sitemap.xml

""".strip()


class RobotsTxtView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse(ROBOTS_TXT_CONTENT, content_type="text/plain")


# ------------


def page_action_create_activity(request, page_id):
    page = get_object_or_404(Page, pk=page_id).specific
    if not page.permissions_for_user(request.user).can_edit():
        raise PermissionDenied

    if activity := create_activity_from_page(page):
        messages.success(request, "Aktivnost (projekt) uspešno ustvarjena.")
        return redirect("wagtailsnippets_home_activity:edit", pk=activity.pk)

    messages.warning(
        request,
        "Aktivnost (projekt) že obstaja ali pa je ni bilo mogoče ustvariti.",
    )
    return redirect("wagtailadmin_pages:edit", page_id=page.pk)


def create_activity_from_page(page):
    if not Activity.objects.filter(page=page).exists():
        activity = Activity.objects.create(
            title=page.title,
            page=page,
            description=page.short_description,
            image=page.thumbnail,
            date=page.published_at,
        )
        activity.pillar_page.set(page.pillar_page.all())
        activity.category.set(page.category.all())
        activity.project.set(page.project.all())
        return activity
    return None
