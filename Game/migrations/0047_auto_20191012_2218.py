# Generated by Django 2.2.3 on 2019-10-12 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0046_auto_20191012_2216'),
    ]

    operations = [
        migrations.RenameField(
            model_name='general',
            old_name='MessageGovernmentScreen',
            new_name='Message_government_page',
        ),
        migrations.RenameField(
            model_name='general',
            old_name='MessageParliamentScreen',
            new_name='Message_parliament_page',
        ),
    ]
