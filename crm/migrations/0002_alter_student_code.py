# Generated by Django 4.1 on 2025-01-25 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='code',
            field=models.CharField(max_length=100, unique=True, verbose_name='Код'),
        ),
    ]
