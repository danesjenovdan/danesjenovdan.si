# Generated by Django 4.2.15 on 2024-10-21 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0079_navigationsettings_new_pages"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="navigationsettings",
            name="pages",
        ),
    ]
