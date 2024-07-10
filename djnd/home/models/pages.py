import icu
from django.core.paginator import Paginator
from django.db import models
from modelcluster.fields import ParentalManyToManyField
from wagtail import blocks
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField, StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.models import Locale, Page

from .blocks import BlogPageBlock, ModuleBlock, PageColors
from .snippets import (
    Activity,
    ActivityCategory,
    ActivityProject,
    TeamMember,
    TeamMemberCategory,
)

sl_collator = icu.Collator.createInstance(icu.Locale("sl_SI"))


class BasePage(Page):
    color = models.CharField(
        max_length=255,
        choices=PageColors.choices,
        default=PageColors.WHITE,
        verbose_name="Barva",
    )

    content_panels = Page.content_panels + [
        FieldPanel("color"),
    ]

    class Meta:
        abstract = True


class HomePage(BasePage):
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
                                choices=PageColors.choices,
                                default=PageColors.WHITE,
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
                        ("linked_sentence", blocks.TextBlock(label="Povezana poved")),
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

    content_panels = BasePage.content_panels + [
        FieldPanel("introduction"),
        FieldPanel("focus_areas_title"),
        FieldPanel("focus_areas"),
        FieldPanel("modules"),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        slovenian_locale = Locale.objects.get(language_code="sl")

        # filtering
        filter = request.GET.get("filter", "all")

        if filter == "promoted":
            activities = Activity.objects.filter(locale=slovenian_locale, promoted=True)
        elif filter == "newsletter":
            try:
                newsletter_project = ActivityProject.objects.get(name="Občasnik")
                activities = Activity.objects.filter(
                    locale=slovenian_locale,
                    project=newsletter_project,
                )
            except:
                activities = Activity.objects.none()
        else:
            activities = Activity.objects.filter(locale=slovenian_locale)

        # get only activities that have english translation
        if request.LANGUAGE_CODE == "en":
            locale = Locale.get_active()
            en_activities_translation_keys = Activity.objects.filter(
                locale=locale
            ).values_list("translation_key", flat=True)
            activities = activities.filter(
                translation_key__in=en_activities_translation_keys
            )

        ordered_activities = activities.order_by("-date")

        paginator = Paginator(ordered_activities, 7)
        activities = paginator.get_page(1)

        context["page_obj"] = activities
        context["activities"] = activities.object_list

        return context


class PillarPage(BasePage):
    lead = models.TextField(blank=True)
    description = RichTextField(blank=True, null=True)
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

    content_panels = BasePage.content_panels + [
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

        slovenian_locale = Locale.objects.get(language_code="sl")

        # get activities for this pillar
        ordered_activities = Activity.objects.filter(
            locale=slovenian_locale,
            pillar_page=self.get_translation(slovenian_locale),
        ).order_by("-date")

        paginator = Paginator(ordered_activities, 7)
        activities = paginator.get_page(1)

        # get activities for this pillar
        context["page_obj"] = activities
        context["activities"] = activities.object_list
        context["loader_extra_query_params"] = f"&pillars={self.id}"

        return context


class ModularPage(BasePage):
    lead = models.TextField(blank=True)
    description = RichTextField(blank=True, null=True)
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

    content_panels = BasePage.content_panels + [
        FieldPanel("lead"),
        FieldPanel("description"),
        FieldPanel("image"),
        FieldPanel("subpages"),
        FieldPanel("modules"),
    ]


class TeamPage(BasePage):
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        lang = request.LANGUAGE_CODE
        locale = Locale.get_active()

        team_member_categories = TeamMemberCategory.objects.filter(locale=locale)
        team_members = TeamMember.objects.filter(locale=locale)
        team_members = sorted(
            team_members,
            key=lambda x: sl_collator.getSortKey(x.name),
        )

        return {
            **context,
            "team_member_categories": team_member_categories,
            "team_members": team_members,
        }


class NewsletterPage(BasePage):
    thumbnail = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    introduction = RichTextField(blank=True, null=True)
    published_at = models.DateField(blank=True, null=True)
    pillar_page = ParentalManyToManyField(
        "home.PillarPage",
        blank=True,
        verbose_name="Tematski sklopi",
    )
    category = ParentalManyToManyField(
        ActivityCategory,
        blank=True,
        verbose_name="Kategorije",
    )
    project = ParentalManyToManyField(
        ActivityProject,
        blank=True,
        verbose_name="Projekti",
    )
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
    promoted = StreamField(
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

    content_panels = BasePage.content_panels + [
        FieldPanel("thumbnail"),
        FieldPanel("published_at"),
        FieldPanel("pillar_page"),
        FieldPanel("category"),
        FieldPanel("project"),
        FieldPanel("introduction"),
        FieldPanel("news"),
        FieldPanel("promoted"),
    ]


class NewsletterListPage(BasePage):
    lead = models.TextField(blank=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    content_panels = BasePage.content_panels + [
        FieldPanel("lead"),
        FieldPanel("image"),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        lang = request.LANGUAGE_CODE
        locale = Locale.get_active()

        newsletters = NewsletterPage.objects.filter(locale=locale).order_by(
            "-published_at"
        )

        return {
            **context,
            "newsletters": newsletters,
        }


class BlogListingPage(BasePage):
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        lang = request.LANGUAGE_CODE
        locale = Locale.get_active()

        blogs = (
            BlogPage.objects.child_of(self)
            .filter(locale=locale)
            .live()
            .order_by("-first_published_at")
        )

        paginator = Paginator(blogs, 7)
        page = request.GET.get("page")
        blogs = paginator.get_page(page)

        return {
            **context,
            "blogs": blogs,
        }


class BlogPage(BasePage):
    short_description = models.TextField(blank=True)
    pillar_page = ParentalManyToManyField(
        "home.PillarPage",
        blank=True,
        verbose_name="Tematski sklopi",
    )
    category = ParentalManyToManyField(
        ActivityCategory,
        blank=True,
        verbose_name="Kategorije",
    )
    project = ParentalManyToManyField(
        ActivityProject,
        blank=True,
        verbose_name="Projekti",
    )
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

    content_panels = BasePage.content_panels + [
        FieldPanel("short_description"),
        FieldPanel("thumbnail"),
        FieldPanel("pillar_page"),
        FieldPanel("category"),
        FieldPanel("project"),
        FieldPanel("modules"),
        FieldPanel("more_blogs"),
    ]


class SupportPage(BasePage):
    lead = models.TextField(blank=True)
    description = RichTextField(blank=True, null=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    content_panels = BasePage.content_panels + [
        FieldPanel("lead"),
        FieldPanel("description"),
        FieldPanel("image"),
    ]


class OurWorkPage(BasePage):
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        # import here because of circular imports
        from home.forms import OurWorkForm

        slovenian_locale = Locale.objects.get(language_code="sl")

        pillars = PillarPage.objects.filter(locale=slovenian_locale)
        categories = ActivityCategory.objects.filter(locale=slovenian_locale)
        projects = ActivityProject.objects.filter(locale=slovenian_locale)

        context["pillars"] = pillars
        context["categories"] = categories
        context["projects"] = projects

        filtered_activities = Activity.objects.filter(locale=slovenian_locale)

        form = OurWorkForm(request.GET, locale=slovenian_locale)
        filtered_activities = form.filter_activities(filtered_activities)

        # get only activities that have english translation
        if request.LANGUAGE_CODE == "en":
            locale = Locale.get_active()
            en_activities_translation_keys = Activity.objects.filter(
                locale=locale
            ).values_list("translation_key", flat=True)
            filtered_activities = filtered_activities.filter(
                translation_key__in=en_activities_translation_keys
            )

        # orderamo
        ordered_activities = filtered_activities.order_by("-date")

        paginator = Paginator(ordered_activities, 7)
        activities = paginator.get_page(1)

        context["form"] = form
        context["page_obj"] = activities
        context["activities"] = activities.object_list

        return context
