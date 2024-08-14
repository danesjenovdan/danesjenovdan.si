from datetime import datetime, timezone

import icu
from django import forms
from django.db import models
from django.http import HttpRequest, HttpResponse
from django.template.defaultfilters import slugify
from django.utils import feedgenerator
from django.utils.http import http_date
from modelcluster.fields import ParentalManyToManyField
from wagtail import blocks
from wagtail.admin.panels import FieldPanel
from wagtail.contrib.routable_page.models import RoutablePageMixin, path
from wagtail.fields import RichTextField, StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.models import Locale, Page
from wagtail.templatetags.wagtailcore_tags import richtext

from ..pagination import get_filtered_activities, paginate_limit_offset
from .blocks import BlogPageBlock, ModuleBlock, PageColors
from .snippets import ActivityCategory, ActivityProject, TeamMember, TeamMemberCategory

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

        activities, _ = get_filtered_activities(request, for_homepage=True)
        activities = paginate_limit_offset(activities, limit=10, offset=0)

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

        # get filtered activities needs a request object so we fake one with the
        # slugified title of the pillar
        fake_request = HttpRequest()
        fake_request.GET.setlist("pillars", [slugify(self.title)])

        activities, _ = get_filtered_activities(fake_request)
        activities = paginate_limit_offset(activities, limit=12, offset=0)

        # get activities for this pillar
        context["page_obj"] = activities
        context["activities"] = activities.object_list
        context["loader_extra_query_params"] = f"&{fake_request.GET.urlencode()}"

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
        FieldPanel("pillar_page", widget=forms.CheckboxSelectMultiple),
        FieldPanel("category", widget=forms.CheckboxSelectMultiple),
        FieldPanel("project", widget=forms.CheckboxSelectMultiple),
        FieldPanel("introduction"),
        FieldPanel("news"),
        FieldPanel("promoted"),
    ]


def subpage_rss(page, subpages, get_description):
    feed = feedgenerator.Rss201rev2Feed(
        title=page.title,
        description=f"RSS feed for {page.title}",
        link=page.full_url,
        feed_url=page.full_url + "rss/",
        language=page.locale.language_code,
    )

    for subpage in subpages:
        timestamp = None
        if subpage.published_at:
            timestamp = datetime.combine(
                subpage.published_at,
                datetime.min.time(),
                tzinfo=timezone.utc,
            )

        feed.add_item(
            title=subpage.title,
            link=subpage.full_url,
            unique_id=subpage.full_url,
            description=get_description(subpage),
            pubdate=timestamp,
        )

    response = HttpResponse(content_type=feed.content_type)
    if len(subpages) > 0:
        response.headers["Last-Modified"] = http_date(
            feed.latest_post_date().timestamp()
        )
    feed.write(response, "utf-8")
    return response


class NewsletterListPage(RoutablePageMixin, BasePage):
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

        locale = Locale.get_active()

        newsletters = (
            NewsletterPage.objects.child_of(self)
            .filter(locale=locale)
            .live()
            .order_by("-published_at", "-first_published_at", "pk")
        )
        newsletters = paginate_limit_offset(newsletters, limit=12, offset=0)

        context["page_obj"] = newsletters
        context["newsletters"] = newsletters.object_list
        context["loader_extra_query_params"] = f"&parent={self.id}"

        return context

    @path("rss/")
    def rss(self, request):
        locale = Locale.get_active()

        newsletters = (
            NewsletterPage.objects.child_of(self)
            .filter(locale=locale)
            .live()
            .order_by("-published_at", "-first_published_at", "pk")
        )
        newsletters = list(newsletters[35:50])

        read_more = "Preberi v celoti" if locale.language_code == "sl" else "Read more"

        def get_description(subpage):
            return f'{richtext(subpage.introduction or "")}<p><a href="{subpage.full_url}">{read_more}</a></p>'

        return subpage_rss(self, newsletters, get_description)


class BlogListingPage(RoutablePageMixin, BasePage):
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

        locale = Locale.get_active()

        blogs = (
            BlogPage.objects.child_of(self)
            .filter(locale=locale)
            .live()
            .order_by("-published_at", "-first_published_at", "pk")
        )
        blogs = paginate_limit_offset(blogs, limit=12, offset=0)

        context["page_obj"] = blogs
        context["blogs"] = blogs.object_list
        context["loader_extra_query_params"] = f"&parent={self.id}"

        return context

    @path("rss/")
    def rss(self, request):
        locale = Locale.get_active()

        blogs = (
            BlogPage.objects.child_of(self)
            .filter(locale=locale)
            .live()
            .order_by("-published_at", "-first_published_at", "pk")
        )
        blogs = list(blogs[:12])

        read_more = "Preberi v celoti" if locale.language_code == "sl" else "Read more"

        def get_description(subpage):
            return f'<p>{subpage.short_description or ""}</p><p><a href="{subpage.full_url}">{read_more}</a></p>'

        return subpage_rss(self, blogs, get_description)


class BlogPage(BasePage):
    short_description = models.TextField(blank=True)
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
        FieldPanel("published_at"),
        FieldPanel("pillar_page", widget=forms.CheckboxSelectMultiple),
        FieldPanel("category", widget=forms.CheckboxSelectMultiple),
        FieldPanel("project", widget=forms.CheckboxSelectMultiple),
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

        slovenian_locale = Locale.objects.get(language_code="sl")

        pillars = PillarPage.objects.filter(locale=slovenian_locale)
        categories = ActivityCategory.objects.filter(locale=slovenian_locale)
        projects = ActivityProject.objects.filter(locale=slovenian_locale)

        context["pillars"] = pillars
        context["categories"] = categories
        context["projects"] = projects

        activities, form = get_filtered_activities(request)
        activities = paginate_limit_offset(activities, limit=10, offset=0)

        context["form"] = form
        context["page_obj"] = activities
        context["activities"] = activities.object_list

        return context
