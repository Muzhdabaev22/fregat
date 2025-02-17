# Generated by Django 4.1 on 2025-01-30 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_alter_student_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='teacher',
            field=models.ManyToManyField(related_name='teacher_related_stud', to='crm.teacher', verbose_name='Учитель'),
        ),
        migrations.AlterField(
            model_name='lessons',
            name='date',
            field=models.DateField(),
        ),
    ]
