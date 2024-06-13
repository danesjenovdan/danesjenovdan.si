# Generated by Django 4.2.10 on 2024-06-13 10:44

from django.db import migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0062_blogpage_category_blogpage_pillar_page_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='category',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='home.activitycategory', verbose_name='Kategorije'),
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='pillar_page',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='home.pillarpage', verbose_name='Tematski sklopi'),
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='project',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='home.activityproject', verbose_name='Projekti'),
        ),
    ]