# Generated by Django 3.2.9 on 2021-12-16 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0016_alter_post_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, db_table='Post_Tags', related_name='posts', to='feed.Tag', verbose_name='تگ\u200cها'),
        ),
    ]