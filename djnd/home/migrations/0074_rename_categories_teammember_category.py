# Generated by Django 4.2.10 on 2024-07-16 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0073_alter_activityproject_options_activityproject_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teammember',
            old_name='categories',
            new_name='category',
        ),
    ]
