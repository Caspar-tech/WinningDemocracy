# Generated by Django 2.2.3 on 2019-10-11 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0034_auto_20191009_0843'),
    ]

    operations = [
        migrations.AddField(
            model_name='parties',
            name='Declaration_maker',
            field=models.BooleanField(default=False),
        ),
    ]