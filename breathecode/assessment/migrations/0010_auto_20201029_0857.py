# Generated by Django 3.1.2 on 2020-10-29 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0009_auto_20201027_0234'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='opened_at',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='status',
            field=models.CharField(choices=[('PENDING', 'Pending'), ('SENT', 'Sent'), ('OPENED', 'Opened'), ('EXPIRED', 'Expired')], default='PENDING', max_length=15),
        ),
    ]