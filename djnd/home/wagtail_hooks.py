from home.models import (
    Activity,
    ActivityCategory,
    ActivityProject,
    Promoted,
    TeamMember,
    TeamMemberCategory,
)
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet


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
