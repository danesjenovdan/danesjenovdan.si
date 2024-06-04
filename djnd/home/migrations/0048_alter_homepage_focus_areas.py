# Generated by Django 4.2.10 on 2024-06-04 10:36

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0047_homepage_focus_areas_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='focus_areas',
            field=wagtail.fields.StreamField([('focus_area', wagtail.blocks.StructBlock([('name', wagtail.blocks.CharBlock(label='Ime')), ('image', wagtail.images.blocks.ImageChooserBlock(label='Ikona')), ('color', wagtail.blocks.ChoiceBlock(choices=[('white', 'Bela'), ('mint', 'Meta'), ('red', 'Rdeča'), ('green', 'Zelena'), ('blue', 'Modra'), ('yellow', 'Rumena'), ('lavender', 'Sivka')], label='Barva')), ('url', wagtail.blocks.URLBlock(label='Zunanja povezava', required=False)), ('page', wagtail.blocks.PageChooserBlock(label='Podstran', required=False))], label='Fokus'))], blank=True, null=True, use_json_field=True, verbose_name='Fokusi'),
        ),
    ]
