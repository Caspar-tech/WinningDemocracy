# Generated by Django 2.2.3 on 2019-10-22 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0062_auto_20191022_1640'),
    ]

    operations = [
        migrations.RenameField(
            model_name='general',
            old_name='Votes_against_proposal',
            new_name='Votes_against_declaration',
        ),
        migrations.RenameField(
            model_name='general',
            old_name='Votes_for_proposal',
            new_name='Votes_for_declaration',
        ),
    ]