# Generated by Django 4.2.10 on 2024-03-27 10:50

import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
import wagtail.snippets.blocks
from django.db import migrations

import home.models.snippets


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0033_delete_donor"),
    ]

    operations = [
        migrations.AlterField(
            model_name="modularpage",
            name="modules",
            field=wagtail.fields.StreamField(
                [
                    ("contact_block", wagtail.blocks.StructBlock([])),
                    (
                        "pillars_block",
                        wagtail.blocks.StructBlock(
                            [
                                ("title", wagtail.blocks.CharBlock()),
                                ("description", wagtail.blocks.TextBlock()),
                                (
                                    "pillars",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.PageChooserBlock(
                                            page_type=["home.PillarPage"]
                                        )
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "networks_block",
                        wagtail.blocks.StructBlock(
                            [
                                ("title", wagtail.blocks.CharBlock()),
                                ("description", wagtail.blocks.TextBlock()),
                                (
                                    "networks",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.StructBlock(
                                            [
                                                ("name", wagtail.blocks.CharBlock()),
                                                (
                                                    "link",
                                                    wagtail.blocks.URLBlock(
                                                        required=False
                                                    ),
                                                ),
                                                (
                                                    "image",
                                                    wagtail.images.blocks.ImageChooserBlock(
                                                        required=False
                                                    ),
                                                ),
                                            ]
                                        )
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "text_content_block",
                        wagtail.blocks.StructBlock(
                            [
                                ("title", wagtail.blocks.CharBlock()),
                                ("text", wagtail.blocks.RichTextBlock()),
                                (
                                    "button",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.StructBlock(
                                            [
                                                (
                                                    "button_text",
                                                    wagtail.blocks.CharBlock(),
                                                ),
                                                (
                                                    "link",
                                                    wagtail.blocks.URLBlock(
                                                        label="Zunanja povezava",
                                                        required=False,
                                                    ),
                                                ),
                                                (
                                                    "page_link",
                                                    wagtail.blocks.PageChooserBlock(
                                                        label="Povezava na stran",
                                                        required=False,
                                                    ),
                                                ),
                                                (
                                                    "color",
                                                    wagtail.blocks.ChoiceBlock(
                                                        choices=[
                                                            ("white", "Bela"),
                                                            ("green", "Zelena"),
                                                        ],
                                                        label="Barva gumba",
                                                    ),
                                                ),
                                            ]
                                        ),
                                        max_num=1,
                                        min_num=0,
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "table_block",
                        wagtail.blocks.StructBlock(
                            [
                                ("title", wagtail.blocks.CharBlock()),
                                (
                                    "table",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.StructBlock(
                                            [
                                                ("title", wagtail.blocks.CharBlock()),
                                                (
                                                    "description",
                                                    wagtail.blocks.TextBlock(),
                                                ),
                                            ]
                                        )
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "donors_block",
                        wagtail.blocks.StructBlock(
                            [
                                ("title", wagtail.blocks.CharBlock()),
                                (
                                    "current_donors",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.StructBlock(
                                            [
                                                ("name", wagtail.blocks.CharBlock()),
                                                (
                                                    "link",
                                                    wagtail.blocks.URLBlock(
                                                        required=False
                                                    ),
                                                ),
                                                (
                                                    "image",
                                                    wagtail.images.blocks.ImageChooserBlock(
                                                        required=False
                                                    ),
                                                ),
                                            ]
                                        )
                                    ),
                                ),
                                (
                                    "past_donors",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.StructBlock(
                                            [
                                                ("name", wagtail.blocks.CharBlock()),
                                                (
                                                    "link",
                                                    wagtail.blocks.URLBlock(
                                                        required=False
                                                    ),
                                                ),
                                                (
                                                    "image",
                                                    wagtail.images.blocks.ImageChooserBlock(
                                                        required=False
                                                    ),
                                                ),
                                            ]
                                        )
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "financial_information_block",
                        wagtail.blocks.StructBlock(
                            [
                                ("title", wagtail.blocks.CharBlock()),
                                (
                                    "reports_url",
                                    wagtail.blocks.URLBlock(
                                        label="Letna vsebinska in finančna poročila",
                                        required=False,
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "promoted_block",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "promoted_snippet",
                                    wagtail.snippets.blocks.SnippetChooserBlock(
                                        home.models.snippets.Promoted
                                    ),
                                )
                            ]
                        ),
                    ),
                ],
                blank=True,
                null=True,
                use_json_field=True,
                verbose_name="Moduli",
            ),
        ),
        migrations.AlterField(
            model_name="pillarpage",
            name="modules",
            field=wagtail.fields.StreamField(
                [
                    ("contact_block", wagtail.blocks.StructBlock([])),
                    (
                        "pillars_block",
                        wagtail.blocks.StructBlock(
                            [
                                ("title", wagtail.blocks.CharBlock()),
                                ("description", wagtail.blocks.TextBlock()),
                                (
                                    "pillars",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.PageChooserBlock(
                                            page_type=["home.PillarPage"]
                                        )
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "networks_block",
                        wagtail.blocks.StructBlock(
                            [
                                ("title", wagtail.blocks.CharBlock()),
                                ("description", wagtail.blocks.TextBlock()),
                                (
                                    "networks",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.StructBlock(
                                            [
                                                ("name", wagtail.blocks.CharBlock()),
                                                (
                                                    "link",
                                                    wagtail.blocks.URLBlock(
                                                        required=False
                                                    ),
                                                ),
                                                (
                                                    "image",
                                                    wagtail.images.blocks.ImageChooserBlock(
                                                        required=False
                                                    ),
                                                ),
                                            ]
                                        )
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "text_content_block",
                        wagtail.blocks.StructBlock(
                            [
                                ("title", wagtail.blocks.CharBlock()),
                                ("text", wagtail.blocks.RichTextBlock()),
                                (
                                    "button",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.StructBlock(
                                            [
                                                (
                                                    "button_text",
                                                    wagtail.blocks.CharBlock(),
                                                ),
                                                (
                                                    "link",
                                                    wagtail.blocks.URLBlock(
                                                        label="Zunanja povezava",
                                                        required=False,
                                                    ),
                                                ),
                                                (
                                                    "page_link",
                                                    wagtail.blocks.PageChooserBlock(
                                                        label="Povezava na stran",
                                                        required=False,
                                                    ),
                                                ),
                                                (
                                                    "color",
                                                    wagtail.blocks.ChoiceBlock(
                                                        choices=[
                                                            ("white", "Bela"),
                                                            ("green", "Zelena"),
                                                        ],
                                                        label="Barva gumba",
                                                    ),
                                                ),
                                            ]
                                        ),
                                        max_num=1,
                                        min_num=0,
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "table_block",
                        wagtail.blocks.StructBlock(
                            [
                                ("title", wagtail.blocks.CharBlock()),
                                (
                                    "table",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.StructBlock(
                                            [
                                                ("title", wagtail.blocks.CharBlock()),
                                                (
                                                    "description",
                                                    wagtail.blocks.TextBlock(),
                                                ),
                                            ]
                                        )
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "donors_block",
                        wagtail.blocks.StructBlock(
                            [
                                ("title", wagtail.blocks.CharBlock()),
                                (
                                    "current_donors",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.StructBlock(
                                            [
                                                ("name", wagtail.blocks.CharBlock()),
                                                (
                                                    "link",
                                                    wagtail.blocks.URLBlock(
                                                        required=False
                                                    ),
                                                ),
                                                (
                                                    "image",
                                                    wagtail.images.blocks.ImageChooserBlock(
                                                        required=False
                                                    ),
                                                ),
                                            ]
                                        )
                                    ),
                                ),
                                (
                                    "past_donors",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.StructBlock(
                                            [
                                                ("name", wagtail.blocks.CharBlock()),
                                                (
                                                    "link",
                                                    wagtail.blocks.URLBlock(
                                                        required=False
                                                    ),
                                                ),
                                                (
                                                    "image",
                                                    wagtail.images.blocks.ImageChooserBlock(
                                                        required=False
                                                    ),
                                                ),
                                            ]
                                        )
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "financial_information_block",
                        wagtail.blocks.StructBlock(
                            [
                                ("title", wagtail.blocks.CharBlock()),
                                (
                                    "reports_url",
                                    wagtail.blocks.URLBlock(
                                        label="Letna vsebinska in finančna poročila",
                                        required=False,
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "promoted_block",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "promoted_snippet",
                                    wagtail.snippets.blocks.SnippetChooserBlock(
                                        home.models.snippets.Promoted
                                    ),
                                )
                            ]
                        ),
                    ),
                ],
                blank=True,
                null=True,
                use_json_field=True,
                verbose_name="Moduli",
            ),
        ),
    ]
