# Generated by Django 4.1 on 2024-08-14 12:30

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_alter_testcinema_question_discusboard'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postblog',
            name='img',
            field=models.ImageField(upload_to='', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='postblog',
            name='text',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Текст'),
        ),
        migrations.CreateModel(
            name='SubStory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('bef_one', models.CharField(max_length=200, verbose_name='before first')),
                ('bef_two', models.CharField(max_length=200, verbose_name='before second')),
                ('bef_three', models.CharField(max_length=200, verbose_name='before third')),
                ('aft_one', models.CharField(max_length=200, verbose_name='after first')),
                ('aft_two', models.CharField(max_length=200, verbose_name='after second')),
                ('aft_three', models.CharField(max_length=200, verbose_name='after third')),
                ('episode', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.episode')),
            ],
        ),
    ]
