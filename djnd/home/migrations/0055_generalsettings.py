# Generated by Django 4.2.10 on 2024-06-12 10:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailcore", "0089_log_entry_data_json_null_to_object"),
        ("home", "0054_supportpage"),
    ]

    operations = [
        migrations.CreateModel(
            name="GeneralSettings",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "support_page",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailcore.page",
                    ),
                ),
            ],
            options={
                "verbose_name": "Splošne nastavitve",
                "verbose_name_plural": "Splošne nastavitve",
            },
        ),
    ]
