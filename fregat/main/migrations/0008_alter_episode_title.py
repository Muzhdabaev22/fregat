# Generated by Django 4.1 on 2023-12-20 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_episode_remove_movie_accent_remove_movie_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='title',
            field=models.CharField(max_length=100, unique=True, verbose_name='Название'),
        ),
    ]