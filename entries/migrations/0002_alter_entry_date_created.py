# Generated by Django 3.2.9 on 2021-11-04 20:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
