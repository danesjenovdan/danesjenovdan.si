# Generated by Django 4.2.10 on 2024-06-12 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0051_alter_modularpage_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='color',
            field=models.CharField(choices=[('white', 'Bela'), ('mint', 'Meta'), ('red', 'Rdeča'), ('green', 'Zelena'), ('blue', 'Modra'), ('yellow', 'Rumena'), ('lavender', 'Sivka')], default='white', max_length=255, verbose_name='Barva'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='color',
            field=models.CharField(choices=[('white', 'Bela'), ('mint', 'Meta'), ('red', 'Rdeča'), ('green', 'Zelena'), ('blue', 'Modra'), ('yellow', 'Rumena'), ('lavender', 'Sivka')], default='white', max_length=255, verbose_name='Barva'),
        ),
        migrations.AddField(
            model_name='modularpage',
            name='color',
            field=models.CharField(choices=[('white', 'Bela'), ('mint', 'Meta'), ('red', 'Rdeča'), ('green', 'Zelena'), ('blue', 'Modra'), ('yellow', 'Rumena'), ('lavender', 'Sivka')], default='white', max_length=255, verbose_name='Barva'),
        ),
        migrations.AddField(
            model_name='newsletterlistpage',
            name='color',
            field=models.CharField(choices=[('white', 'Bela'), ('mint', 'Meta'), ('red', 'Rdeča'), ('green', 'Zelena'), ('blue', 'Modra'), ('yellow', 'Rumena'), ('lavender', 'Sivka')], default='white', max_length=255, verbose_name='Barva'),
        ),
        migrations.AddField(
            model_name='newsletterpage',
            name='color',
            field=models.CharField(choices=[('white', 'Bela'), ('mint', 'Meta'), ('red', 'Rdeča'), ('green', 'Zelena'), ('blue', 'Modra'), ('yellow', 'Rumena'), ('lavender', 'Sivka')], default='white', max_length=255, verbose_name='Barva'),
        ),
        migrations.AddField(
            model_name='pillarpage',
            name='color',
            field=models.CharField(choices=[('white', 'Bela'), ('mint', 'Meta'), ('red', 'Rdeča'), ('green', 'Zelena'), ('blue', 'Modra'), ('yellow', 'Rumena'), ('lavender', 'Sivka')], default='white', max_length=255, verbose_name='Barva'),
        ),
        migrations.AddField(
            model_name='teampage',
            name='color',
            field=models.CharField(choices=[('white', 'Bela'), ('mint', 'Meta'), ('red', 'Rdeča'), ('green', 'Zelena'), ('blue', 'Modra'), ('yellow', 'Rumena'), ('lavender', 'Sivka')], default='white', max_length=255, verbose_name='Barva'),
        ),
    ]
