# Generated by Django 4.2.1 on 2023-05-28 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facilities', '0006_rename_addr_likesresult_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='likesresult',
            name='address',
        ),
    ]