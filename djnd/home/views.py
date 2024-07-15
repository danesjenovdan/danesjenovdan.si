from django.views.generic import ListView

from .models.snippets import Activity
from .pagination import get_filtered_activities


class ActivityView(ListView):
    model = Activity
    template_name = "home/activities.html"
    context_object_name = "activities"
    paginate_by = 7
    ordering = ["-date"]

    def get_queryset(self):
        activities, form = get_filtered_activities(self.request)
        return activities


class ActivityHomepageView(ListView):
    model = Activity
    template_name = "home/activities-homepage.html"
    context_object_name = "activities"
    paginate_by = 7
    ordering = ["-date"]

    def get_queryset(self):
        activities, form = get_filtered_activities(self.request, for_homepage=True)
        return activities
