# Generated by Django 3.2.8 on 2021-10-26 04:40

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0002_auto_20211026_0934'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CustomProfile',
            new_name='CustomrProfile',
        ),
    ]
