# Generated by Django 2.2.3 on 2019-09-03 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0006_general_gamename'),
    ]

    operations = [
        migrations.AddField(
            model_name='representatives',
            name='party',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Game.Parties'),
        ),
    ]
