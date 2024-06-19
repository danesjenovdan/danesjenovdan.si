from django import forms

from home.models import PillarPage, ActivityCategory, ActivityProject


class OurWorkForm(forms.Form):

    def __init__(self, *args, **kwargs):
        self.locale = kwargs.pop('locale')
        super(OurWorkForm, self).__init__(*args, **kwargs)
        self.fields['pillars'].queryset = PillarPage.objects.filter(locale=self.locale)
        self.fields['categories'].queryset = ActivityCategory.objects.filter(locale=self.locale)
        self.fields['projects'].queryset = ActivityProject.objects.filter(locale=self.locale)

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
