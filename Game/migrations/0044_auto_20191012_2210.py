# Generated by Django 2.2.3 on 2019-10-12 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0043_auto_20191012_2206'),
    ]

    operations = [
        migrations.RenameField(
            model_name='counties',
            old_name='representative',
            new_name='Representative',
        ),
    ]