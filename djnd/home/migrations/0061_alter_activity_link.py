# Generated by Django 4.2.10 on 2024-06-13 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0060_activity_page_alter_activity_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='link',
            field=models.URLField(blank=True, null=True, verbose_name='Zunanja povezava'),
        ),
    ]
