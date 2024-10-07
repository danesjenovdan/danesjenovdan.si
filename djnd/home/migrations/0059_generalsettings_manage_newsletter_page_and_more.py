# Generated by Django 4.2.10 on 2024-06-13 09:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailcore", "0089_log_entry_data_json_null_to_object"),
        ("home", "0058_alter_blogpage_modules_alter_homepage_modules_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="generalsettings",
            name="manage_newsletter_page",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailcore.page",
                verbose_name="Urejanje naročnine na novičnike",
            ),
        ),
        migrations.AddField(
            model_name="generalsettings",
            name="privacy_policy_page",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailcore.page",
                verbose_name="Politika zasebnosti in varstva osebnih podatkov",
            ),
        ),
        migrations.AlterField(
            model_name="generalsettings",
            name="our_work_page",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailcore.page",
                verbose_name="Naše delo",
            ),
        ),
        migrations.AlterField(
            model_name="generalsettings",
            name="support_page",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailcore.page",
                verbose_name="Podpri nas",
            ),
        ),
    ]
