# Generated by Django 3.1.6 on 2021-02-21 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20210221_2138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='views',
        ),
    ]
