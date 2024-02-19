from django.db import models

from wagtail import blocks
from wagtail.contrib.settings.models import (
    BaseGenericSetting,
    register_setting,
)
from wagtail.fields import StreamField
from wagtail.admin.panels import (
    FieldPanel,
)


@register_setting
class HeaderSettings(BaseGenericSetting):
    pillars = StreamField(
        [
            ("page", blocks.PageChooserBlock()),
        ],
        verbose_name="Stebri",
        use_json_field=True,
    )

    panels = [
        FieldPanel("pillars"),
    ]
