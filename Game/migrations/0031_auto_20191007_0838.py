# Generated by Django 2.2.3 on 2019-10-07 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0030_auto_20190924_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='general',
            name='Community_bar',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='general',
            name='Ethics_bar',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='general',
            name='Immigration_bar',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='general',
            name='Nature_bar',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='general',
            name='Social_protection_bar',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='general',
            name='Taxation_bar',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='general',
            name='Worldview_bar',
            field=models.IntegerField(default=0),
        ),
    ]
