# Generated by Django 2.2.3 on 2019-10-22 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0060_general_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='parties',
            name='Next_action',
            field=models.IntegerField(default=0),
        ),
    ]