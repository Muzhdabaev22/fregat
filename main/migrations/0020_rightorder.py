# Generated by Django 4.1 on 2024-08-23 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_alter_postblog_img_alter_postblog_text_substory'),
    ]

    operations = [
        migrations.CreateModel(
            name='RightOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200, verbose_name='Вопрос')),
                ('priority', models.IntegerField(verbose_name='Приоритет')),
                ('episode', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.episode')),
            ],
        ),
    ]