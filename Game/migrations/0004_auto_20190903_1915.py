# Generated by Django 2.2.3 on 2019-09-03 17:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Game', '0003_game'),
    ]

    operations = [
        migrations.CreateModel(
            name='General',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('turn', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='Game',
        ),
        migrations.RemoveField(
            model_name='representatives',
            name='player',
        ),
        migrations.AddField(
            model_name='representatives',
            name='user',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]