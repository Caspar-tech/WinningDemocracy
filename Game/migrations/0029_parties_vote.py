# Generated by Django 2.2.3 on 2019-09-23 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0028_auto_20190922_2037'),
    ]

    operations = [
        migrations.AddField(
            model_name='parties',
            name='Vote',
            field=models.TextField(default='Yes'),
            preserve_default=False,
        ),
    ]