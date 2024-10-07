# Generated by Django 4.2.10 on 2024-06-02 06:33

from django.db import migrations
import home.models.snippets
import wagtail.blocks
import wagtail.fields
import wagtail.snippets.blocks


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0041_blogpage_thumbnail"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogpage",
            name="modules",
            field=wagtail.fields.StreamField(
                [
                    (
                        "text_content_block",
                        wagtail.blocks.StructBlock(
                            [
                                ("title", wagtail.blocks.CharBlock(required=False)),
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
                    ("newsletter_block", wagtail.blocks.StructBlock([])),
                    (
                        "support_block",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "color_scheme",
                                    wagtail.blocks.ChoiceBlock(
                                        choices=[("red", "Rdeča"), ("green", "Zelena")],
                                        label="Barvna shema",
                                    ),
                                )
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
