# Generated by Django 2.2.3 on 2019-07-22 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('weekly_amount', models.IntegerField()),
                ('capacity', models.IntegerField()),
                ('searchable', models.BooleanField(default=True)),
            ],
        ),
    ]