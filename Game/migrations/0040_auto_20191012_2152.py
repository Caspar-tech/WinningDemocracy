# Generated by Django 2.2.3 on 2019-10-12 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0039_auto_20191012_1525'),
    ]

    operations = [
        migrations.RenameField(
            model_name='counties',
            old_name='name',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='parties',
            old_name='name',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='representatives',
            old_name='name',
            new_name='Name',
        ),
    ]
