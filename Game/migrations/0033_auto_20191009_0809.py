# Generated by Django 2.2.3 on 2019-10-09 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0032_auto_20191008_0953'),
    ]

    operations = [
        migrations.AddField(
            model_name='parties',
            name='Government',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='parties',
            name='PrimeMinister',
            field=models.BooleanField(default=False),
        ),
    ]
