from django.db import models

from wagtail.fields import StreamField
from wagtail.models import Page
from wagtail import blocks
from wagtail.admin.panels import FieldPanel
from wagtail.images.blocks import ImageChooserBlock

from .blocks import ModuleBlock


class HomePage(Page):
    pass


# class OurWorkPage(Page):
#     pass


class PillarPage(Page):
    subtitle = models.TextField(blank=True)
    description = models.TextField(blank=True)
    image = models.ForeignKey(
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
                        ("name", blocks.CharBlock()),
                        ("description", blocks.CharBlock()),
                        ("image", ImageChooserBlock()),
                        # url?
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
        FieldPanel("subtitle"),
        FieldPanel("description"),
        FieldPanel("image"),
        FieldPanel("projects"),
        FieldPanel("modules"),
    ]


class ModularPage(Page):
    pass


class NewsletterPage(Page):
    pass


class BlogPage(Page):
    pass
