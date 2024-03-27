from django import forms

from home.models import PillarPage, ActivityCategory, ActivityProject


class OurWorkForm(forms.Form):
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
