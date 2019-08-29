# Generated by Django 2.2.4 on 2019-08-29 01:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0008_group_members'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='members',
            field=models.ManyToManyField(blank=True, default='', related_name='group_member', to=settings.AUTH_USER_MODEL),
        ),
    ]
