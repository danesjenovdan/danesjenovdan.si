from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet

from home.models import (
    Activity,
    ActivityCategory,
    ActivityProject,
    Promoted,
    TeamMember,
    TeamMemberCategory,
)


class ActivityViewSet(SnippetViewSet):
    model = Activity
    list_display = ["title", "date", "promoted"]
    list_filter = ["promoted", "pillar_page", "category", "project"]


register_snippet(ActivityViewSet)
register_snippet(ActivityCategory)
register_snippet(ActivityProject)
register_snippet(Promoted)
register_snippet(TeamMember)
register_snippet(TeamMemberCategory)
