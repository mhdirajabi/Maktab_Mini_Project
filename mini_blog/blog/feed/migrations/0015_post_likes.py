# Generated by Django 3.2.9 on 2021-12-15 19:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feed', '0014_auto_20211215_1751'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(db_table='Post_likes', related_name='liked_posts', to=settings.AUTH_USER_MODEL, verbose_name='لایک\u200cها'),
        ),
    ]