# Generated by Django 2.2.3 on 2019-09-03 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0005_auto_20190903_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='general',
            name='gamename',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
