# Generated by Django 4.2.10 on 2024-05-16 16:01

import django.db.models.deletion
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailimages", "0025_alter_image_file_alter_rendition_file"),
        ("home", "0035_promoted_activity_alter_promoted_description_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="activitycategory",
            options={"verbose_name": "Kategorija", "verbose_name_plural": "Kategorije"},
        ),
        migrations.AlterModelOptions(
            name="activityproject",
            options={"verbose_name": "Projekt", "verbose_name_plural": "Projekti"},
        ),
        migrations.AlterField(
            model_name="pillarpage",
            name="projects",
            field=wagtail.fields.StreamField(
                [
                    (
                        "project",
                        wagtail.blocks.StructBlock(
                            [
                                ("name", wagtail.blocks.CharBlock(label="Ime")),
                                ("description", wagtail.blocks.CharBlock(label="Opis")),
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
                            label="Projekt",
                        ),
                    )
                ],
                blank=True,
                null=True,
                use_json_field=True,
                verbose_name="Projekti",
            ),
        ),
        migrations.AlterField(
            model_name="promoted",
            name="activity",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="home.activity",
                verbose_name="Aktivnost",
            ),
        ),
        migrations.AlterField(
            model_name="promoted",
            name="description",
            field=models.CharField(blank=True, verbose_name="Opis"),
        ),
        migrations.AlterField(
            model_name="promoted",
            name="image",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailimages.image",
                verbose_name="Slika",
            ),
        ),
        migrations.AlterField(
            model_name="promoted",
            name="link",
            field=models.URLField(blank=True, verbose_name="Povezava"),
        ),
        migrations.AlterField(
            model_name="promoted",
            name="title",
            field=models.TextField(
                blank=True,
                help_text="Če so polja prazna in obstaja Aktivnost, se uporabijo podatki Aktivnosti",
                verbose_name="Naslov",
            ),
        ),
    ]
