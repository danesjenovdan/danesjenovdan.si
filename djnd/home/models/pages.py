from django.db import models
from wagtail import blocks
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField, StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.models import Locale, Page

from .blocks import ModuleBlock, BlogPageBlock
from .snippets import TeamMember, TeamMemberCategory, Activity


class HomePage(Page):
    introduction = RichTextField(blank=True, null=True)
    focus_areas_title = models.CharField(max_length=255, blank=True, null=True)
    focus_areas = StreamField(
        [
            (
                "focus_area",
                blocks.StructBlock(
                    [
                        ("name", blocks.CharBlock(label="Ime")),
                        ("image", ImageChooserBlock(label="Ikona")),
                        (
                            "color",
                            blocks.ChoiceBlock(
                                choices=[
                                    ("white", "Bela"),
                                    ("mint", "Meta"),
                                    ("red", "Rdeča"),
                                    ("green", "Zelena"),
                                    ("blue", "Modra"),
                                    ("yellow", "Rumena"),
                                    ("lavender", "Sivka"),
                                ],
                                default="white",
                                label="Barva",
                            ),
                        ),
                        (
                            "url",
                            blocks.URLBlock(label="Zunanja povezava", required=False),
                        ),
                        (
                            "page",
                            blocks.PageChooserBlock(label="Podstran", required=False),
                        ),
                    ],
                    label="Fokus",
                ),
            )
        ],
        null=True,
        blank=True,
        use_json_field=True,
        verbose_name="Fokusi",
    )

    modules = StreamField(
        ModuleBlock(), verbose_name="Moduli", null=True, blank=True, use_json_field=True
    )

    content_panels = Page.content_panels + [
        FieldPanel("introduction"),
        FieldPanel("focus_areas_title"),
        FieldPanel("focus_areas"),
        FieldPanel("modules"),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        # get activities for this pillar
        context["activities"] = Activity.objects.all().order_by("-date")[:7]

        return context


class PillarPage(Page):
    lead = models.TextField(blank=True)
    description = models.TextField(blank=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    icon = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    projects = StreamField(
        [
            (
                "project",
                blocks.StructBlock(
                    [
                        ("name", blocks.CharBlock(label="Ime")),
                        ("description", blocks.CharBlock(label="Opis")),
                        ("image", ImageChooserBlock(label="Ikona")),
                        (
                            "url",
                            blocks.URLBlock(label="Zunanja povezava", required=False),
                        ),
                        (
                            "page",
                            blocks.PageChooserBlock(label="Podstran", required=False),
                        ),
                    ],
                    label="Projekt",
                ),
            )
        ],
        null=True,
        blank=True,
        use_json_field=True,
        verbose_name="Projekti",
    )
    modules = StreamField(
        ModuleBlock(), verbose_name="Moduli", null=True, blank=True, use_json_field=True
    )
    activities_title = models.TextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("lead"),
        FieldPanel("description"),
        FieldPanel("image"),
        FieldPanel("icon"),
        FieldPanel("projects"),
        FieldPanel("modules"),
        FieldPanel("activities_title"),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        # get activities for this pillar
        context["activities"] = Activity.objects.filter(pillar_page=self).order_by(
            "-date"
        )[:9]

        return context


class ModularPage(Page):
    lead = models.TextField(blank=True)
    description = models.TextField(blank=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    subpages = StreamField(
        [
            (
                "page",
                blocks.StructBlock(
                    [
                        ("name", blocks.CharBlock()),
                        ("description", blocks.TextBlock()),
                        ("icon", ImageChooserBlock()),
                        ("page", blocks.PageChooserBlock()),
                    ]
                ),
            )
        ],
        null=True,
        blank=True,
        use_json_field=True,
    )
    modules = StreamField(
        ModuleBlock(), verbose_name="Moduli", null=True, blank=True, use_json_field=True
    )

    content_panels = Page.content_panels + [
        FieldPanel("lead"),
        FieldPanel("description"),
        FieldPanel("image"),
        FieldPanel("subpages"),
        FieldPanel("modules"),
    ]


class TeamPage(Page):
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        lang = request.LANGUAGE_CODE
        locale = Locale.get_active()

        team_member_categories = TeamMemberCategory.objects.filter(locale=locale)
        team_members = TeamMember.objects.filter(locale=locale)

        return {
            **context,
            "team_member_categories": team_member_categories,
            "team_members": team_members,
        }


class NewsletterPage(Page):
    thumbnail = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    introduction = RichTextField(blank=True, null=True)
    news = StreamField(
        [
            (
                "article",
                blocks.StructBlock(
                    [
                        ("name", blocks.CharBlock()),
                        ("description", blocks.CharBlock()),
                        ("image", ImageChooserBlock()),
                        ("link", blocks.URLBlock(required=False)),
                    ]
                ),
            )
        ],
        null=True,
        blank=True,
        use_json_field=True,
    )
    promoted_blogs = StreamField(
        [
            (
                "blogpage",
                blocks.PageChooserBlock(
                    target_model="home.BlogPage"
                ),
            )
        ],
        verbose_name="Povezani zapisi",
        null=True,
        blank=True,
        use_json_field=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("thumbnail"),
        FieldPanel("introduction"),
        FieldPanel("news"),
        FieldPanel("promoted_blogs"),
    ]


class BlogPage(Page):
    short_description = models.TextField(blank=True)
    modules = StreamField(
        BlogPageBlock(),
        verbose_name="Moduli",
        null=True,
        blank=True,
        use_json_field=True,
    )
    more_blogs = StreamField(
        [
            (
                "blogpage",
                blocks.PageChooserBlock(target_model="home.BlogPage"),
            )
        ],
        verbose_name="Povezani zapisi",
        null=True,
        blank=True,
        use_json_field=True,
    )
    thumbnail = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    content_panels = Page.content_panels + [
        FieldPanel("thumbnail"),
        FieldPanel("short_description"),
        FieldPanel("modules"),
        FieldPanel("more_blogs"),
    ]
