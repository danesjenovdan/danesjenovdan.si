from wagtail import blocks
from wagtail.admin.panels import FieldPanel
from wagtail.contrib.settings.models import BaseGenericSetting, register_setting
from wagtail.fields import StreamField

from .pages import PillarPage


@register_setting
class NavigationSettings(BaseGenericSetting):
    pillars = StreamField(
        [
            ("page", blocks.PageChooserBlock(PillarPage)),
        ],
        verbose_name="Stebri",
        use_json_field=True,
    )
    pages = StreamField(
        [
            ("page", blocks.StructBlock([
                ("page", blocks.PageChooserBlock()),
                ("subpages", blocks.ListBlock(blocks.PageChooserBlock())),
            ])),
        ],
        verbose_name="Strani",
        use_json_field=True,
        null=True,
    )

    panels = [
        FieldPanel("pillars"),
        FieldPanel("pages"),
    ]

    class Meta:
        verbose_name = "Navigacija"
        verbose_name_plural = "Navigacija"
