# Generated by Django 2.2.3 on 2019-10-12 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0040_auto_20191012_2152'),
    ]

    operations = [
        migrations.RenameField(
            model_name='parties',
            old_name='PrimeMinister',
            new_name='Prime_minister',
        ),
    ]
