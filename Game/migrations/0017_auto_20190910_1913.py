# Generated by Django 2.2.3 on 2019-09-10 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0016_topics_current_topic'),
    ]

    operations = [
        migrations.AddField(
            model_name='general',
            name='Military',
            field=models.IntegerField(default=50),
        ),
        migrations.AddField(
            model_name='general',
            name='Nature',
            field=models.IntegerField(default=50),
        ),
        migrations.AddField(
            model_name='general',
            name='Taxes',
            field=models.IntegerField(default=50),
        ),
    ]