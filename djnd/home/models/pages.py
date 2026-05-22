import re
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
from .settings import GeneralSettings
from .snippets import ActivityCategory, ActivityProject, TeamMember, TeamMemberCategory

sl_collator = icu.Collator.createInstance(icu.Locale("sl_SI"))


class BasePage(Page):
    color = models.CharField(
        max_length=255,
        choices=PageColors.choices,
        default=PageColors.WHITE,
        verbose_name="Barva",
    )
    meta_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="OG slika",
    )

    content_panels = Page.content_panels + [
        FieldPanel("color"),
    ]

    promote_panels = Page.promote_panels + [
        FieldPanel("meta_image"),
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
        activities = paginate_limit_offset(activities, limit=16, offset=0)

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
    filter_icon = models.ForeignKey(
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
        FieldPanel("filter_icon"),
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
        activities = paginate_limit_offset(activities, limit=18, offset=0)

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
    short_description = RichTextField(blank=True, null=True)
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
                        ("image", ImageChooserBlock(required=False)),
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
                        ("image", ImageChooserBlock(required=False)),
                        ("link", blocks.URLBlock(required=False)),
                    ]
                ),
            )
        ],
        null=True,
        blank=True,
        use_json_field=True,
    )
    custom_sections = StreamField(
        [
            (
                "section",
                blocks.StructBlock(
                    [
                        ("section_name", blocks.CharBlock()),
                        ("section_description", blocks.CharBlock()),
                        (
                            "section_display",
                            blocks.ChoiceBlock(
                                choices=[
                                    ("list", "List"),
                                    ("grid", "Grid"),
                                    ("text", "Text"),
                                ],
                                default="list",
                            ),
                        ),
                        (
                            "section_items",
                            blocks.ListBlock(
                                blocks.StructBlock(
                                    [
                                        ("name", blocks.CharBlock()),
                                        (
                                            "description",
                                            blocks.RichTextBlock(
                                                features=[
                                                    "bold",
                                                    "italic",
                                                    "link",
                                                    "ul",
                                                    "ol",
                                                ]
                                            ),
                                        ),
                                        ("image", ImageChooserBlock(required=False)),
                                        ("link", blocks.URLBlock(required=False)),
                                    ]
                                )
                            ),
                        ),
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
        FieldPanel("short_description"),
        FieldPanel("published_at"),
        FieldPanel("pillar_page", widget=forms.CheckboxSelectMultiple),
        FieldPanel("category", widget=forms.CheckboxSelectMultiple),
        FieldPanel("project", widget=forms.CheckboxSelectMultiple),
        FieldPanel("introduction"),
        FieldPanel("news"),
        FieldPanel("promoted"),
        FieldPanel("custom_sections"),
    ]


def subpage_rss(page, subpages, get_description, get_full_url):
    if page.seo_title:
        title = page.seo_title
    else:
        title = page.title
        site = page.get_site()
        if site and site.site_name:
            title = f"{site.site_name} | {title}"

    feed = feedgenerator.Rss201rev2Feed(
        title=title,
        description=f"{page.title} RSS feed",
        link=page.full_url,
        feed_url=page.full_url + "rss/",
        language=page.locale.language_code,
    )

    for subpage in subpages:
        timestamp = None
        if hasattr(subpage, "published_at") and subpage.published_at:
            timestamp = datetime.combine(
                subpage.published_at,
                datetime.min.time(),
                tzinfo=timezone.utc,
            )
        elif hasattr(subpage, "date") and subpage.date:
            timestamp = datetime.combine(
                subpage.date,
                datetime.min.time(),
                tzinfo=timezone.utc,
            )

        full_url = get_full_url(subpage)

        feed.add_item(
            title=subpage.title,
            link=full_url,
            unique_id=full_url,
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
    is_programmers_newsletter = models.BooleanField(
        default=False,
        verbose_name="Ali je to programerski novičnik",
    )

    content_panels = BasePage.content_panels + [
        FieldPanel("lead"),
        FieldPanel("image"),
        FieldPanel("is_programmers_newsletter"),
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
        newsletters = paginate_limit_offset(newsletters, limit=18, offset=0)

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
        newsletters = list(newsletters[:12])

        read_more = "Preberi v celoti" if locale.language_code == "sl" else "Read more"

        def get_full_url(subpage):
            return subpage.full_url

        def get_description(subpage):
            desc = ""
            if subpage.thumbnail:
                rendition = subpage.thumbnail.get_rendition("fill-1200x630")
                if rendition and rendition.url and rendition.url.startswith("http"):
                    desc += f'<p><a href="{get_full_url(subpage)}"><img src="{rendition.url}" alt="{rendition.alt}"></a></p>'
            desc += richtext(subpage.short_description or "")
            return f'{desc}<p><a href="{get_full_url(subpage)}">{read_more}</a></p>'

        return subpage_rss(self, newsletters, get_description, get_full_url)


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
        blogs = paginate_limit_offset(blogs, limit=18, offset=0)

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

        def get_full_url(subpage):
            return subpage.full_url

        def get_description(subpage):
            desc = ""
            if subpage.thumbnail:
                rendition = subpage.thumbnail.get_rendition("fill-1200x630")
                if rendition and rendition.url and rendition.url.startswith("http"):
                    desc += f'<p><a href="{get_full_url(subpage)}"><img src="{rendition.url}" alt="{rendition.alt}"></a></p>'
            desc += f'<p>{subpage.short_description or ""}</p>'
            return f'{desc}<p><a href="{get_full_url(subpage)}">{read_more}</a></p>'

        return subpage_rss(self, blogs, get_description, get_full_url)


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

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        if category := ActivityCategory.objects.filter(name="Zapis").first():
            if category_local := category.localized:
                general_settings = GeneralSettings.load(request_or_site=request)
                page_url = general_settings.our_work_page.localized.get_url(request)
                context["more_blogs_link"] = (
                    f"{page_url}?categories={slugify(category_local.name)}"
                )

        return context


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


class OurWorkPage(RoutablePageMixin, BasePage):
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        sl = Locale.objects.get(language_code="sl")

        pillars = PillarPage.objects.filter(locale=sl)
        categories = ActivityCategory.objects.filter(locale=sl).order_by("sort_order")
        projects = ActivityProject.objects.filter(locale=sl).order_by("sort_order")

        context["pillars"] = pillars
        context["categories"] = categories
        context["projects"] = projects

        activities, form = get_filtered_activities(request)
        activities = paginate_limit_offset(activities, limit=16, offset=0)

        context["form"] = form
        context["page_obj"] = activities
        context["activities"] = activities.object_list

        return context

    @path("rss/")
    def rss(self, request):
        locale = Locale.get_active()

        activities, form = get_filtered_activities(request)
        activities = list(activities[:12])

        read_more = "Poglej tukaj!" if locale.language_code == "sl" else "Take a look!"

        def get_full_url(snippet):
            if snippet.page:
                return snippet.page.full_url
            elif snippet.link:
                return snippet.link
            return self.full_url

        def get_description(snippet):
            desc = ""
            if snippet.image:
                rendition = snippet.image.get_rendition("fill-1200x630")
                if rendition and rendition.url and rendition.url.startswith("http"):
                    desc += f'<p><a href="{get_full_url(snippet)}"><img src="{rendition.url}" alt="{rendition.alt}"></a></p>'
            desc += f'<p>{snippet.description or ""}</p>'
            desc += richtext(snippet.note or "")
            return f'{desc}<p><a href="{get_full_url(snippet)}">{read_more}</a></p>'

        return subpage_rss(self, activities, get_description, get_full_url)
