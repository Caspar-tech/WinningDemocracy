# Generated by Django 2.2.3 on 2019-10-24 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0065_auto_20191023_0824'),
    ]

    operations = [
        migrations.AddField(
            model_name='general',
            name='Message_propose_deal',
            field=models.TextField(default='yes'),
            preserve_default=False,
        ),
    ]
