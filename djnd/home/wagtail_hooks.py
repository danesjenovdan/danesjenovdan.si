from wagtail.snippets.models import register_snippet

from home.models import (
    ActivityCategory,
    ActivityProject,
    Activity,
    Network,
    Donor,
    TeamMemberCategory,
    TeamMember,
)

register_snippet(ActivityCategory)
register_snippet(ActivityProject)
register_snippet(Activity)
register_snippet(Network)
register_snippet(Donor)
register_snippet(TeamMemberCategory)
register_snippet(TeamMember)
