# Generated by Django 4.1 on 2023-11-26 11:33

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postblog',
            name='text',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
