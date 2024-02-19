# Generated by Django 4.2.10 on 2024-02-18 21:40

from django.db import migrations, models
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_alter_blogpage_modules_alter_modularpage_modules_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeaderSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pillars', wagtail.fields.StreamField([('page', wagtail.blocks.PageChooserBlock())], use_json_field=True, verbose_name='Stebri')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]