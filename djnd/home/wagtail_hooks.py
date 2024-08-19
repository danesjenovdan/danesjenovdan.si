from wagtail import hooks
from wagtail.rich_text import LinkHandler
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet

from django.utils.html import escape

from .forms import (
    ActivityAdminModelForm,
    BlogPageAdminPageForm,
    NewsletterPageAdminPageForm,
    TeamMemberAdminModelForm,
)
from .models.pages import BlogPage, NewsletterPage
from .models.snippets import (
    Activity,
    ActivityCategory,
    ActivityProject,
    Promoted,
    TeamMember,
    TeamMemberCategory,
)

BlogPage.base_form_class = BlogPageAdminPageForm
NewsletterPage.base_form_class = NewsletterPageAdminPageForm

Activity.base_form_class = ActivityAdminModelForm
TeamMember.base_form_class = TeamMemberAdminModelForm


class ActivityViewSet(SnippetViewSet):
    model = Activity
    list_display = ["title", "date", "promoted"]
    list_filter = {
        "title": ["icontains"],
        "promoted": ["exact"],
        "pillar_page": ["exact"],
        "category": ["exact"],
        "project": ["exact"],
    }


class ActivityCategoryViewSet(SnippetViewSet):
    model = ActivityCategory
    list_display = ["name", "order"]


class ActivityProjectViewSet(SnippetViewSet):
    model = ActivityProject
    list_display = ["name", "order"]


register_snippet(ActivityViewSet)
register_snippet(ActivityCategoryViewSet)
register_snippet(ActivityProjectViewSet)
register_snippet(Promoted)
register_snippet(TeamMember)
register_snippet(TeamMemberCategory)


class NewTabExternalLinkHandler(LinkHandler):
    identifier = 'external'

    @classmethod
    def expand_db_attributes(cls, attrs):
        href = attrs['href']
        return '<a href="%s" target="_blank">' % escape(href)


@hooks.register("register_rich_text_features")
def more_rich_text_features(features):
    features.default_features.append("blockquote")

    features.register_link_type(NewTabExternalLinkHandler)
    
