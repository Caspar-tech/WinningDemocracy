# Generated by Django 2.2.3 on 2019-10-12 20:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0042_auto_20191012_2200'),
    ]

    operations = [
        migrations.RenameField(
            model_name='representatives',
            old_name='party',
            new_name='Party',
        ),
    ]
