from django.views.generic import TemplateView
from django.shortcuts import render, redirect

from wagtail.models import Locale


from home.forms import OurWorkForm
from home.models import Activity


class OurWorkView(TemplateView):
    template_name = "home/our_work_page.html"

    def get(self, request, *args, **kwargs):
        lang = request.LANGUAGE_CODE
        locale = Locale.get_active()

        form = OurWorkForm(locale=locale)

        activities = Activity.objects.all()

        return render(
            request,
            self.template_name,
            {"form": form, "activities": activities},
        )

    def post(self, request, *args, **kwargs):
        lang = request.LANGUAGE_CODE
        locale = Locale.get_active()
        
        form = OurWorkForm(request.POST, locale=locale)

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
