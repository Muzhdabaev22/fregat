# Generated by Django 4.1 on 2023-12-07 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_postblog_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postblog',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]