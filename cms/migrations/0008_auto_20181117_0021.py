# Generated by Django 2.1.3 on 2018-11-17 00:21

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cms', '0007_auto_20181113_1719'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Article',
        ),
    ]