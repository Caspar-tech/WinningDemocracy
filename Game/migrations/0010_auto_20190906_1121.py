# Generated by Django 2.2.3 on 2019-09-06 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0009_representatives_countyelection'),
    ]

    operations = [
        migrations.RenameField(
            model_name='counties',
            old_name='PC',
            new_name='CP',
        ),
        migrations.RenameField(
            model_name='parties',
            old_name='PC',
            new_name='CP',
        ),
        migrations.RenameField(
            model_name='representatives',
            old_name='PC',
            new_name='CP',
        ),
    ]
