# Generated by Django 3.2.9 on 2021-12-17 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_alter_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, null=True, verbose_name='درباره من'),
        ),
    ]
