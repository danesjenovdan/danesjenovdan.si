# Generated by Django 4.2.10 on 2024-06-06 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0048_remove_newsletterpage_exposed_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsletterpage',
            name='published_at',
            field=models.DateField(blank=True, null=True),
        ),
    ]
