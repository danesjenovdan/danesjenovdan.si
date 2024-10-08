# Generated by Django 4.2.10 on 2024-06-13 10:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailcore", "0089_log_entry_data_json_null_to_object"),
        ("home", "0059_generalsettings_manage_newsletter_page_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="activity",
            name="page",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailcore.page",
                verbose_name="Povezava na podstran",
            ),
        ),
        migrations.AlterField(
            model_name="activity",
            name="link",
            field=models.URLField(verbose_name="Zunanja povezava"),
        ),
    ]
