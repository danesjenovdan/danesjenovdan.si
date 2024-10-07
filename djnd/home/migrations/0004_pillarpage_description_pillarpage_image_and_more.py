# Generated by Django 4.2.10 on 2024-02-14 10:40

import django.db.models.deletion
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailimages", "0025_alter_image_file_alter_rendition_file"),
        ("home", "0003_blogpage_modularpage_newsletterpage_pillarpage"),
    ]

    operations = [
        migrations.AddField(
            model_name="pillarpage",
            name="description",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="pillarpage",
            name="image",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailimages.image",
            ),
        ),
        migrations.AddField(
            model_name="pillarpage",
            name="modules",
            field=wagtail.fields.StreamField(
                [], null=True, use_json_field=True, verbose_name="Moduli"
            ),
        ),
        migrations.AddField(
            model_name="pillarpage",
            name="projects",
            field=wagtail.fields.StreamField(
                [
                    (
                        "project",
                        wagtail.blocks.StructBlock(
                            [
                                ("name", wagtail.blocks.CharBlock()),
                                ("description", wagtail.blocks.CharBlock()),
                                ("image", wagtail.images.blocks.ImageChooserBlock()),
                            ]
                        ),
                    )
                ],
                null=True,
                use_json_field=True,
            ),
        ),
        migrations.AddField(
            model_name="pillarpage",
            name="subtitle",
            field=models.TextField(blank=True),
        ),
    ]
