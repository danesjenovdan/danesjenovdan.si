from django.views.generic import TemplateView
from django.shortcuts import render, redirect

from home.forms import OurWorkForm
from home.models import Activity


class OurWorkView(TemplateView):
    template_name = "home/our_work_page.html"

    def get(self, request, *args, **kwargs):
        form = OurWorkForm()

        activities = Activity.objects.all()

        return render(
            request,
            self.template_name,
            {"form": form, "activities": activities},
        )

    def post(self, request, *args, **kwargs):
        form = OurWorkForm(request.POST)

        activities = Activity.objects.all()

        if form.is_valid():
            pillars = form.cleaned_data["pillars"]
            categories = form.cleaned_data["categories"]
            projects = form.cleaned_data["projects"]

            if pillars:
                activities = activities.filter(pillar_page__in=pillars)

            if categories:
                activities = activities.filter(category__in=categories)

            if projects:
                activities = activities.filter(project__in=projects)

        return render(
            request,
            self.template_name,
            {"form": form, "activities": activities},
        )
