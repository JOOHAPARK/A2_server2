# Generated by Django 4.2.1 on 2023-05-28 08:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('facilities', '0003_remove_likes_name_likes_like'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikesResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like_state', models.BooleanField()),
                ('addr', models.CharField(max_length=200)),
                ('lat', models.CharField(max_length=100)),
                ('lon', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='likes',
            name='liked_users',
            field=models.ManyToManyField(blank=True, related_name='liked_infos', to=settings.AUTH_USER_MODEL),
        ),
    ]