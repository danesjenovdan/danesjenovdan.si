from django.views.generic import ListView
from django.shortcuts import render, redirect

from .models.snippets import Activity


class ActivityView(ListView):
    model = Activity
    template_name = "home/activities.html"
    context_object_name = "activities"
    paginate_by = 7
    ordering = ['-date']