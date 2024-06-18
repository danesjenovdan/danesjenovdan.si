from django.views.generic import ListView
from django.shortcuts import render, redirect

from wagtail.models import Locale

from home.models import Activity
from home.forms import OurWorkForm


class ActivityView(ListView):
    model = Activity
    template_name = "home/activities.html"
    context_object_name = "activities"
    paginate_by = 7
    ordering = ['-date']

    def get_queryset(self):
        lang = self.request.LANGUAGE_CODE
        locale = Locale.get_active()

        form = OurWorkForm(self.request.GET, locale=locale)

        filtered_activities = Activity.objects.filter(locale=locale)

        if form.is_valid():
            pillars = form.cleaned_data["pillars"]
            categories = form.cleaned_data["categories"]
            projects = form.cleaned_data["projects"]

            if pillars:
                filtered_activities = filtered_activities.filter(pillar_page__in=pillars)

            if categories:
                filtered_activities = filtered_activities.filter(category__in=categories)

            if projects:
                filtered_activities = filtered_activities.filter(project__in=projects)

        activities = filtered_activities.order_by("-date")

        return activities