import icu
from django.db import models
from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

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

        all_activities = Activity.objects.all().order_by("-date")
        paginator = Paginator(all_activities, 7)
        page = request.GET.get("page")
        try:
            activities = paginator.page(page)
        except PageNotAnInteger:
            activities = paginator.page(1)
        except EmptyPage:
            activities = paginator.page(paginator.num_pages)

        context["activities"] = activities

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

        # get activities for this pillar
        context["activities"] = Activity.objects.filter(pillar_page=self).order_by(
            "-date"
        )[:9]

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
    def serve(self, request):
        from home.forms import OurWorkForm

        lang = request.LANGUAGE_CODE
        locale = Locale.get_active()

        if request.method == "POST":
            form = OurWorkForm(request.POST, locale=locale)

            filtered_activities = Activity.objects.all()

            if form.is_valid():
                pillars = form.cleaned_data["pillars"]
                categories = form.cleaned_data["categories"]
                projects = form.cleaned_data["projects"]

                if pillars:
                    filtered_activities = filtered_activities.filter(pillar_page__in=pillars)

                if categories:
                    filtered_activities = filtered_activities.filter(category__in=categories)

                if projects:
                    filtered_activities = filtered_activities.filter(project__in=projects)

            ordered_activities = filtered_activities.order_by("-date")

            paginator = Paginator(ordered_activities, 7)
            page = request.GET.get("page")

            try:
                # If the page exists and the ?page=x is an int
                activities = paginator.page(page)
            except PageNotAnInteger:
                # If the ?page=x is not an int; show the first page
                activities = paginator.page(1)
            except EmptyPage:
                # If the ?page=x is out of range (too high most likely)
                # Then return the last page
                activities = paginator.page(paginator.num_pages)

            return render(
                request,
                self.get_template(request),
                {"page": self, "form": form, "activities": activities},
            )
        else:
            form = OurWorkForm(locale=locale)

            all_activities = Activity.objects.all().order_by("-date")

            paginator = Paginator(all_activities, 7)
            page = request.GET.get("page")

            try:
                # If the page exists and the ?page=x is an int
                activities = paginator.page(page)
            except PageNotAnInteger:
                # If the ?page=x is not an int; show the first page
                activities = paginator.page(1)
            except EmptyPage:
                # If the ?page=x is out of range (too high most likely)
                # Then return the last page
                activities = paginator.page(paginator.num_pages)
        
            return render(
                request,
                self.get_template(request),
                {"page": self, "form": form, "activities": activities},
            )
