# Generated by Django 3.1.6 on 2021-02-21 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_topic_views'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='img',
        ),
    ]