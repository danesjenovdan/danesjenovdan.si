# Generated by Django 4.2.15 on 2024-09-02 11:25

import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0077_bloglistingpage_meta_image_blogpage_meta_image_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="newsletterpage",
            name="short_description",
            field=wagtail.fields.RichTextField(blank=True, null=True),
        ),
    ]
