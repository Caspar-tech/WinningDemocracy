# Generated by Django 2.2.3 on 2019-09-11 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0019_auto_20190911_1045'),
    ]

    operations = [
        migrations.AddField(
            model_name='topics',
            name='Parent',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
