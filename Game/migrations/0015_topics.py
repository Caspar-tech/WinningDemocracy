# Generated by Django 2.2.3 on 2019-09-10 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0014_parties_seats'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Vote', models.TextField()),
                ('CP', models.IntegerField()),
                ('LR', models.IntegerField()),
                ('New', models.BooleanField(default=True)),
            ],
        ),
    ]
