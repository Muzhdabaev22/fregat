# Generated by Django 4.1 on 2023-12-22 17:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_episode_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='img',
            field=models.ImageField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
    ]
