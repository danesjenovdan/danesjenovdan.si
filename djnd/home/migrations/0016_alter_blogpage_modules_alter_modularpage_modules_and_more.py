# Generated by Django 4.2.10 on 2024-02-18 09:58

import wagtail.blocks
import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0015_alter_blogpage_modules_alter_modularpage_modules_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogpage",
            name="modules",
            field=wagtail.fields.StreamField(
                [
                    ("newsletter_block", wagtail.blocks.StructBlock([])),
                    (
                        "pillars_block",
                        wagtail.blocks.StructBlock(
                            [
                                ("title", wagtail.blocks.CharBlock()),
                                ("description", wagtail.blocks.TextBlock()),
                                (
                                    "pillars",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.PageChooserBlock()
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
                            ]
                        ),
                    ),
                    (
                        "text_content_block",
                        wagtail.blocks.StructBlock(
                            [
                                ("title", wagtail.blocks.CharBlock()),
                                ("text", wagtail.blocks.RichTextBlock()),
                            ]
                        ),
                    ),
                    (
                        "donors_block",
                        wagtail.blocks.StructBlock(
                            [("title", wagtail.blocks.CharBlock())]
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
            model_name="modularpage",
            name="modules",
            field=wagtail.fields.StreamField(
                [
                    ("newsletter_block", wagtail.blocks.StructBlock([])),
                    (
                        "pillars_block",
                        wagtail.blocks.StructBlock(
                            [
                                ("title", wagtail.blocks.CharBlock()),
                                ("description", wagtail.blocks.TextBlock()),
                                (
                                    "pillars",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.PageChooserBlock()
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
                            ]
                        ),
                    ),
                    (
                        "text_content_block",
                        wagtail.blocks.StructBlock(
                            [
                                ("title", wagtail.blocks.CharBlock()),
                                ("text", wagtail.blocks.RichTextBlock()),
                            ]
                        ),
                    ),
                    (
                        "donors_block",
                        wagtail.blocks.StructBlock(
                            [("title", wagtail.blocks.CharBlock())]
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
                    ("newsletter_block", wagtail.blocks.StructBlock([])),
                    (
                        "pillars_block",
                        wagtail.blocks.StructBlock(
                            [
                                ("title", wagtail.blocks.CharBlock()),
                                ("description", wagtail.blocks.TextBlock()),
                                (
                                    "pillars",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.PageChooserBlock()
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
                            ]
                        ),
                    ),
                    (
                        "text_content_block",
                        wagtail.blocks.StructBlock(
                            [
                                ("title", wagtail.blocks.CharBlock()),
                                ("text", wagtail.blocks.RichTextBlock()),
                            ]
                        ),
                    ),
                    (
                        "donors_block",
                        wagtail.blocks.StructBlock(
                            [("title", wagtail.blocks.CharBlock())]
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
