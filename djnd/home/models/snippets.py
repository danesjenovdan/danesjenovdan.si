from django.db import models

from wagtail.models import TranslatableMixin


class ActivityCategory(TranslatableMixin, models.Model):
    name = models.TextField()

    def __str__(self) -> str:
        return self.name

    class Meta(TranslatableMixin.Meta):
        verbose_name = "Kategorija"
        verbose_name_plural = "Kategorije"


class ActivityProject(TranslatableMixin, models.Model):
    name = models.TextField()

    def __str__(self) -> str:
        return self.name

    class Meta(TranslatableMixin.Meta):
        verbose_name = "Projekt"
        verbose_name_plural = "Projekti"


class Activity(TranslatableMixin, models.Model):
    title = models.TextField()
    link = models.URLField()
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
    note = models.TextField(blank=True)
    source = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.title

    class Meta(TranslatableMixin.Meta):
        verbose_name = "Aktivnost"
        verbose_name_plural = "Aktivnosti"


class TeamMemberCategory(TranslatableMixin, models.Model):
    name = models.TextField()

    def __str__(self) -> str:
        return self.name

    class Meta(TranslatableMixin.Meta):
        verbose_name = "Vloga člana ekipe"
        verbose_name_plural = "Vloge članov ekipe"


class TeamMember(TranslatableMixin, models.Model):
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
    categories = models.ManyToManyField(TeamMemberCategory, blank=True)

    def __str__(self) -> str:
        return self.name

    class Meta(TranslatableMixin.Meta):
        verbose_name = "Član ekipe"
        verbose_name_plural = "Člani ekipe"


class Promoted(TranslatableMixin, models.Model):
    title = models.TextField(blank=True, verbose_name="Naslov", help_text="Če so polja prazna in obstaja Aktivnost, se uporabijo podatki Aktivnosti")
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
        verbose_name="Aktivnost",
    )

    def __str__(self) -> str:
        if self.activity:
            return self.title if self.title else self.activity.title
        else:
            return self.title

    class Meta(TranslatableMixin.Meta):
        verbose_name = "Izpostavljeno"
        verbose_name_plural = "Izpostavljeno"
