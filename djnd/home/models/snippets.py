from django import forms
from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.models import Orderable, TranslatableMixin
from wagtail.search import index


class ActivityCategory(TranslatableMixin, Orderable):
    name = models.TextField()
    icon = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def cache_key(self):
        return f"activity_category_{self.id}_{self.updated_at.timestamp()}"

    def __str__(self) -> str:
        return self.name

    class Meta(TranslatableMixin.Meta):
        verbose_name = "Kategorija"
        verbose_name_plural = "Kategorije"


class ActivityProject(TranslatableMixin, Orderable):
    name = models.TextField()
    icon = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def cache_key(self):
        return f"activity_project_{self.id}_{self.updated_at.timestamp()}"

    def __str__(self) -> str:
        return self.name

    class Meta(TranslatableMixin.Meta):
        verbose_name = "Projekt"
        verbose_name_plural = "Projekti"


class Activity(index.Indexed, TranslatableMixin, models.Model):
    title = models.TextField()
    link = models.URLField(verbose_name="Zunanja povezava", null=True, blank=True)
    page = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Povezava na podstran",
    )
    description = models.TextField(blank=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    pillar_page = models.ManyToManyField("home.PillarPage", blank=True)
    category = models.ManyToManyField(ActivityCategory, blank=True)
    project = models.ManyToManyField(ActivityProject, blank=True)
    date = models.DateField(null=True, blank=True)
    note = RichTextField(null=True, blank=True)
    promoted = models.BooleanField(default=False)

    panels = [
        FieldPanel("title"),
        FieldPanel("link"),
        FieldPanel("page"),
        FieldPanel("description"),
        FieldPanel("image"),
        FieldPanel("pillar_page", widget=forms.CheckboxSelectMultiple),
        FieldPanel("category", widget=forms.CheckboxSelectMultiple),
        FieldPanel("project", widget=forms.CheckboxSelectMultiple),
        FieldPanel("date"),
        FieldPanel("note"),
        FieldPanel("promoted"),
    ]

    search_fields = [
        index.SearchField("title"),
        index.AutocompleteField("title"),
        index.FilterField("locale_id"),
    ]

    def __str__(self) -> str:
        return self.title

    class Meta(TranslatableMixin.Meta):
        verbose_name = "Aktivnost (Projekt)"
        verbose_name_plural = "Aktivnosti (Projekti)"


class TeamMemberCategory(TranslatableMixin, models.Model):
    name = models.TextField()

    def __str__(self) -> str:
        return self.name

    class Meta(TranslatableMixin.Meta):
        verbose_name = "Vloga člana ekipe"
        verbose_name_plural = "Vloge članov ekipe"


class TeamMember(index.Indexed, TranslatableMixin, models.Model):
    name = models.TextField()
    email = models.TextField(blank=True)
    role = models.TextField(blank=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    category = models.ManyToManyField(TeamMemberCategory, blank=True)

    panels = [
        FieldPanel("name"),
        FieldPanel("email"),
        FieldPanel("role"),
        FieldPanel("image"),
        FieldPanel("category", widget=forms.CheckboxSelectMultiple),
    ]

    search_fields = [
        index.SearchField("name"),
        index.AutocompleteField("name"),
        index.FilterField("locale_id"),
    ]

    def __str__(self) -> str:
        return self.name

    class Meta(TranslatableMixin.Meta):
        verbose_name = "Član ekipe"
        verbose_name_plural = "Člani ekipe"


class Promoted(TranslatableMixin, models.Model):
    title = models.TextField(
        blank=True,
        verbose_name="Naslov",
        help_text="Če so polja prazna in obstaja Aktivnost (Projekt), se uporabijo podatki Aktivnosti (Projekta)",
    )
    description = models.CharField(
        blank=True,
        verbose_name="Opis",
    )
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Slika",
    )
    link = models.URLField(
        blank=True,
        verbose_name="Povezava",
    )
    activity = models.ForeignKey(
        Activity,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Aktivnost (Projekt)",
    )

    def __str__(self) -> str:
        if self.activity:
            return self.title if self.title else self.activity.title
        else:
            return self.title

    class Meta(TranslatableMixin.Meta):
        verbose_name = "Izpostavljeno"
        verbose_name_plural = "Izpostavljeno"
