# Generated by Django 4.2.10 on 2024-06-02 06:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailimages", "0025_alter_image_file_alter_rendition_file"),
        ("home", "0040_blogpage_more_blogs_alter_blogpage_modules_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="blogpage",
            name="thumbnail",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailimages.image",
            ),
        ),
    ]
