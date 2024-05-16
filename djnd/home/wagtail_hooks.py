from wagtail.snippets.models import register_snippet

from home.models import (
    ActivityCategory,
    ActivityProject,
    Activity,
    TeamMemberCategory,
    TeamMember,
    Promoted,
)

register_snippet(ActivityCategory)
register_snippet(ActivityProject)
register_snippet(Activity)
register_snippet(TeamMemberCategory)
register_snippet(TeamMember)
register_snippet(Promoted)
