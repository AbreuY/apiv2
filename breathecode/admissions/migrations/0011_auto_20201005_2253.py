# Generated by Django 3.1.1 on 2020-10-05 22:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('admissions', '0010_auto_20200929_1812'),
    ]

    operations = [
        migrations.AddField(
            model_name='academy',
            name='active_campaign_slug',
            field=models.SlugField(default=django.utils.timezone.now, max_length=100, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='certificate',
            name='schedule_type',
            field=models.CharField(choices=[('PART-TIME', 'Part-Time'), ('FULL-TIME', 'Full-Time')], default='part-time', max_length=15),
            preserve_default=False,
        ),
    ]