# Generated by Django 2.2.3 on 2019-09-14 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0022_auto_20190912_2007'),
    ]

    operations = [
        migrations.AddField(
            model_name='general',
            name='CP',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='general',
            name='LR',
            field=models.IntegerField(default=0),
        ),
    ]