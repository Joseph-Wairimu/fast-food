# Generated by Django 4.0.4 on 2022-04-21 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='items_json',
        ),
    ]
