from django.views.generic import ListView
from django.shortcuts import render, redirect

from wagtail.models import Locale

from home.models import Activity, ActivityProject, ActivityCategory
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

        slovenian_locale = Locale.objects.get(language_code='sl')

        # our work page filtering
        form = OurWorkForm(self.request.GET, locale=slovenian_locale)
        filtered_activities = Activity.objects.filter(locale=slovenian_locale)
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
        
        # homepage filtering
        filter = self.request.GET.get('filter', '')
        if filter == "projects":
            # TODO: filtering by DJND project
            djnd_project = ActivityProject.objects.get(name="DJND projekt")
            filtered_activities = Activity.objects.filter(locale=slovenian_locale, project=djnd_project)
        elif filter == "newsletter":
            newsletter_category = ActivityCategory.objects.get(name="Občasnik")
            filtered_activities = Activity.objects.filter(locale=slovenian_locale, category=newsletter_category)

        activities = filtered_activities.order_by("-date")

        return activities