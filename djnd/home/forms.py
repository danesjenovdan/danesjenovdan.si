from django import forms
from django.template.defaultfilters import slugify
from wagtail.admin.forms.models import WagtailAdminModelForm
from wagtail.admin.forms.pages import WagtailAdminPageForm
from wagtail.models import Locale

from .models.pages import PillarPage
from .models.snippets import (ActivityCategory, ActivityProject,
                              TeamMemberCategory)

#
# ADMIN FORMS
#


# SNIPPET FORMS
class ActivityAdminModelForm(WagtailAdminModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # filter querysets based on locale
        sl = Locale.objects.get(language_code="sl")
        self.fields["pillar_page"].queryset = PillarPage.objects.filter(locale=sl)
        self.fields["category"].queryset = ActivityCategory.objects.filter(locale=sl)
        self.fields["project"].queryset = ActivityProject.objects.filter(locale=sl)


class TeamMemberAdminModelForm(WagtailAdminModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # filter querysets based on locale
        sl = Locale.objects.get(language_code="sl")
        self.fields["category"].queryset = TeamMemberCategory.objects.filter(locale=sl)


# PAGE FORMS
class ActivityTagPageAdminPageForm(WagtailAdminPageForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # filter querysets based on locale
        sl = Locale.objects.get(language_code="sl")
        self.fields["pillar_page"].queryset = PillarPage.objects.filter(locale=sl)
        self.fields["category"].queryset = ActivityCategory.objects.filter(locale=sl)
        self.fields["project"].queryset = ActivityProject.objects.filter(locale=sl)


class BlogPageAdminPageForm(ActivityTagPageAdminPageForm):
    pass


class NewsletterPageAdminPageForm(ActivityTagPageAdminPageForm):
    pass


#
# FORMS
#

FIELD_TO_MODEL = {
    "pillars": PillarPage,
    "categories": ActivityCategory,
    "projects": ActivityProject,
}

FIELD_TO_NAME = {
    "pillars": "title",
    "categories": "name",
    "projects": "name",
}


class OurWorkForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.locale = kwargs.pop("locale")

        # map slugs to ids in query
        if args and args[0]:
            querydict_ids = self.map_query_dict_slugs(args[0])
            args = (querydict_ids,) + args[1:]

        super().__init__(*args, **kwargs)

        # filter querysets based on locale
        for field_name, Model in FIELD_TO_MODEL.items():
            self.fields[field_name].queryset = Model.objects.filter(locale=self.locale)

    pillars = forms.ModelMultipleChoiceField(
        required=False,
        queryset=PillarPage.objects,
        widget=forms.CheckboxSelectMultiple(attrs={"class": ""}),
    )
    categories = forms.ModelMultipleChoiceField(
        required=False,
        queryset=ActivityCategory.objects,
        widget=forms.CheckboxSelectMultiple(attrs={"class": ""}),
    )
    projects = forms.ModelMultipleChoiceField(
        required=False,
        queryset=ActivityProject.objects,
        widget=forms.CheckboxSelectMultiple(attrs={"class": ""}),
    )
    promoted = forms.BooleanField(required=False)

    def map_query_dict_slugs(self, querydict):
        querydict = querydict.copy()  # original is immutable
        for key in querydict:
            values = self.map_slugs_to_ids(key, querydict.getlist(key))
            querydict.setlist(key, values)
        return querydict

    def map_slugs_to_ids(self, field_name, slugs):
        if not slugs:
            return []
        if field_name not in FIELD_TO_MODEL:
            return slugs

        Model = FIELD_TO_MODEL[field_name]
        name = FIELD_TO_NAME[field_name]
        objects = Model.objects.all()
        slug_to_id = {
            slugify(getattr(obj, name)): str(
                obj.get_translation_or_none(self.locale).id
            )
            for obj in objects
            if obj.get_translation_or_none(self.locale)
        }
        return [slug_to_id.get(slug, slug) for slug in slugs]

    def filter_activities(self, activities):
        if self.is_valid():
            pillars = self.cleaned_data["pillars"]
            categories = self.cleaned_data["categories"]
            projects = self.cleaned_data["projects"]
            promoted = self.cleaned_data["promoted"]

            if pillars:
                activities = activities.filter(pillar_page__in=pillars)

            if categories:
                activities = activities.filter(category__in=categories)

            if projects:
                activities = activities.filter(project__in=projects)

            if promoted:
                activities = activities.filter(promoted=True)

        return activities.distinct()
