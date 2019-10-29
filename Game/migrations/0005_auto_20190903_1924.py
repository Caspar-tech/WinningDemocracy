# Generated by Django 2.2.3 on 2019-09-03 17:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Game', '0004_auto_20190903_1915'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='representatives',
            name='user',
        ),
        migrations.CreateModel(
            name='Parties',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('PC', models.IntegerField()),
                ('LR', models.IntegerField()),
                ('user', models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
