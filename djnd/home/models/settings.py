from django.db import models
from wagtail import blocks
from wagtail.admin.panels import FieldPanel
from wagtail.contrib.settings.models import BaseGenericSetting, register_setting
from wagtail.fields import StreamField

from .blocks import NavigationPageWithSubpagesBlock
from .pages import PillarPage


@register_setting
class GeneralSettings(BaseGenericSetting):
    our_work_page = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Naše delo",
    )

    support_page = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Podpri nas",
    )

    privacy_policy_page = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Politika zasebnosti in varstva osebnih podatkov",
    )

    manage_newsletter_page = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Urejanje naročnine na novičnike",
    )

    panels = [
        FieldPanel("our_work_page"),
        FieldPanel("support_page"),
        FieldPanel("privacy_policy_page"),
        FieldPanel("manage_newsletter_page"),
    ]

    class Meta:
        verbose_name = "Splošne nastavitve"
        verbose_name_plural = "Splošne nastavitve"


@register_setting
class NavigationSettings(BaseGenericSetting):
    pillars = StreamField(
        [
            ("page", blocks.PageChooserBlock(PillarPage)),
        ],
        verbose_name="Stebri",
        use_json_field=True,
    )
    new_pages = StreamField(
        [
            ("page", NavigationPageWithSubpagesBlock()),
        ],
        verbose_name="Strani",
        use_json_field=True,
        null=True,
    )

    panels = [
        FieldPanel("pillars"),
        FieldPanel("new_pages"),
    ]

    class Meta:
        verbose_name = "Navigacija"
        verbose_name_plural = "Navigacija"
