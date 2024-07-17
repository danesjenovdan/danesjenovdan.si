from django.urls import path

from . import views

urlpatterns = [
    path("activities/", views.ActivityView.as_view(), name="activities"),
    path("activities-homepage/", views.ActivityHomepageView.as_view(), name="activities-homepage"),
    path("newsletters/", views.NewsletterListView.as_view(), name="newsletters"),
    path("blogs/", views.BlogListView.as_view(), name="blogs"),
]
