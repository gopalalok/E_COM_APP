# Generated by Django 3.1.4 on 2021-02-10 19:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20210211_0112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderidmerge',
            name='dtime',
        ),
        migrations.AddField(
            model_name='order',
            name='dtime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
