# Generated by Django 2.2.3 on 2019-10-16 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0052_auto_20191016_1053'),
    ]

    operations = [
        migrations.AddField(
            model_name='parties',
            name='Made_deal',
            field=models.TextField(default='No'),
        ),
    ]
