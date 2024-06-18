from django.urls import path

from . import views

urlpatterns = [
  path("activities/", views.ActivityView.as_view(), name="activities"),
]