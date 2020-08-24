# Generated by Django 3.0.7 on 2020-07-08 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0017_auto_20200619_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='automation',
            name='slug',
            field=models.SlugField(blank=True, default='', help_text='unique string id that is used to connect incoming leads to automations', max_length=150),
        ),
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(max_length=150, unique=True),
        ),
    ]