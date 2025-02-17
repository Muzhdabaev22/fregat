# Generated by Django 4.1 on 2025-02-04 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0004_alter_lessons_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='city',
            field=models.CharField(default=1, max_length=100, verbose_name='Город'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='contacts',
            field=models.CharField(default=2, max_length=100, verbose_name='Контакты'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='image',
            field=models.ImageField(default=1, upload_to='', verbose_name='Изображение'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='start_point',
            field=models.TextField(default=5, verbose_name='Начальный уровень'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='surname',
            field=models.CharField(default=1, max_length=100, verbose_name='Фамилия'),
            preserve_default=False,
        ),
    ]
