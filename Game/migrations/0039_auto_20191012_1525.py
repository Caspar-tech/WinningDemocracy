# Generated by Django 2.2.3 on 2019-10-12 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0038_auto_20191011_1557'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='general',
            name='Community',
        ),
        migrations.RemoveField(
            model_name='general',
            name='Community_bar',
        ),
        migrations.RemoveField(
            model_name='general',
            name='Community_govt',
        ),
    ]
