# Generated by Django 4.2.10 on 2024-02-18 10:18

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_alter_blogpage_modules_alter_modularpage_modules_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='modules',
            field=wagtail.fields.StreamField([('newsletter_block', wagtail.blocks.StructBlock([])), ('pillars_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('description', wagtail.blocks.TextBlock()), ('pillars', wagtail.blocks.ListBlock(wagtail.blocks.PageChooserBlock()))])), ('networks_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('description', wagtail.blocks.TextBlock())])), ('text_content_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('text', wagtail.blocks.RichTextBlock()), ('button', wagtail.blocks.StructBlock([('button_text', wagtail.blocks.CharBlock()), ('link', wagtail.blocks.URLBlock(label='Zunanja povezava', required=False)), ('page_link', wagtail.blocks.PageChooserBlock(label='Povezava na stran', required=False)), ('color', wagtail.blocks.ChoiceBlock(choices=['white', 'green']))], required=False))])), ('donors_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock())])), ('financial_information_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('reports_url', wagtail.blocks.URLBlock(label='Letna vsebinska in finančna poročila', required=False))]))], blank=True, null=True, use_json_field=True, verbose_name='Moduli'),
        ),
        migrations.AlterField(
            model_name='modularpage',
            name='modules',
            field=wagtail.fields.StreamField([('newsletter_block', wagtail.blocks.StructBlock([])), ('pillars_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('description', wagtail.blocks.TextBlock()), ('pillars', wagtail.blocks.ListBlock(wagtail.blocks.PageChooserBlock()))])), ('networks_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('description', wagtail.blocks.TextBlock())])), ('text_content_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('text', wagtail.blocks.RichTextBlock()), ('button', wagtail.blocks.StructBlock([('button_text', wagtail.blocks.CharBlock()), ('link', wagtail.blocks.URLBlock(label='Zunanja povezava', required=False)), ('page_link', wagtail.blocks.PageChooserBlock(label='Povezava na stran', required=False)), ('color', wagtail.blocks.ChoiceBlock(choices=['white', 'green']))], required=False))])), ('donors_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock())])), ('financial_information_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('reports_url', wagtail.blocks.URLBlock(label='Letna vsebinska in finančna poročila', required=False))]))], blank=True, null=True, use_json_field=True, verbose_name='Moduli'),
        ),
        migrations.AlterField(
            model_name='pillarpage',
            name='modules',
            field=wagtail.fields.StreamField([('newsletter_block', wagtail.blocks.StructBlock([])), ('pillars_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('description', wagtail.blocks.TextBlock()), ('pillars', wagtail.blocks.ListBlock(wagtail.blocks.PageChooserBlock()))])), ('networks_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('description', wagtail.blocks.TextBlock())])), ('text_content_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('text', wagtail.blocks.RichTextBlock()), ('button', wagtail.blocks.StructBlock([('button_text', wagtail.blocks.CharBlock()), ('link', wagtail.blocks.URLBlock(label='Zunanja povezava', required=False)), ('page_link', wagtail.blocks.PageChooserBlock(label='Povezava na stran', required=False)), ('color', wagtail.blocks.ChoiceBlock(choices=['white', 'green']))], required=False))])), ('donors_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock())])), ('financial_information_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('reports_url', wagtail.blocks.URLBlock(label='Letna vsebinska in finančna poročila', required=False))]))], blank=True, null=True, use_json_field=True, verbose_name='Moduli'),
        ),
    ]
