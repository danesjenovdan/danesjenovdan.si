# Generated by Django 4.2.10 on 2024-06-04 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0046_homepage_focus_areas'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='focus_areas_title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]