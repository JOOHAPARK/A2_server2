# Generated by Django 4.2.1 on 2023-05-29 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='username_comment',
            field=models.CharField(max_length=100, null=True),
        ),
    ]