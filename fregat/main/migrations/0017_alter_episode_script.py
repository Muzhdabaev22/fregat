# Generated by Django 4.1 on 2024-08-04 15:33

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_episode_script'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='script',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
