# Generated by Django 2.2.3 on 2019-10-09 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0033_auto_20191009_0809'),
    ]

    operations = [
        migrations.AddField(
            model_name='general',
            name='Community_govt',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='general',
            name='Ethics_govt',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='general',
            name='Immigration_govt',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='general',
            name='Nature_govt',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='general',
            name='Social_protection_govt',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='general',
            name='Taxation_govt',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='general',
            name='Worldview_govt',
            field=models.TextField(default=''),
        ),
    ]
