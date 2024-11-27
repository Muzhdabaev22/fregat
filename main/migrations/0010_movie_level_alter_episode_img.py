# Generated by Django 4.1 on 2024-01-02 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_episode_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='level',
            field=models.ManyToManyField(related_name='lvl_movie', to='main.level', verbose_name='Уровень'),
        ),
        migrations.AlterField(
            model_name='episode',
            name='img',
            field=models.ImageField(upload_to='', verbose_name='Изображение'),
        ),
    ]