# Generated by Django 2.2.3 on 2019-10-20 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0057_counties_spread'),
    ]

    operations = [
        migrations.AddField(
            model_name='general',
            name='Test',
            field=models.BooleanField(default=False),
        ),
    ]
