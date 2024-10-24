# Generated by Django 4.2.10 on 2024-06-04 10:21

import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0045_homepage_introduction"),
    ]

    operations = [
        migrations.AddField(
            model_name="homepage",
            name="focus_areas",
            field=wagtail.fields.StreamField(
                [
                    (
                        "focus_area",
                        wagtail.blocks.StructBlock(
                            [
                                ("name", wagtail.blocks.CharBlock(label="Ime")),
                                (
                                    "image",
                                    wagtail.images.blocks.ImageChooserBlock(
                                        label="Ikona"
                                    ),
                                ),
                                (
                                    "url",
                                    wagtail.blocks.URLBlock(
                                        label="Zunanja povezava", required=False
                                    ),
                                ),
                                (
                                    "page",
                                    wagtail.blocks.PageChooserBlock(
                                        label="Podstran", required=False
                                    ),
                                ),
                            ],
                            label="Fokus",
                        ),
                    )
                ],
                blank=True,
                null=True,
                use_json_field=True,
                verbose_name="Fokusi",
            ),
        ),
    ]
