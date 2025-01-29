from django.db import models

class Admin(models.Model):
    username = models.CharField("Логин", max_length=100, unique=True, default=None)
    name = models.CharField("Имя", max_length=100)

    def __str__(self):
        return f"{self.name}"
    
class Teacher(models.Model):
    username = models.CharField("Логин", max_length=100, unique=True, default=None)
    name = models.CharField("Имя", max_length=100)

    def __str__(self):
        return f"{self.name}"
    
class Student(models.Model):
    username = models.CharField("Логин", max_length=100, unique=True, default=None)
    name = models.CharField("Имя", max_length=100)
    code = models.CharField("Код", max_length=100, unique=True)
    
    def __str__(self):
        return f"{self.name}"
    
    
class Lessons(models.Model):
    
    status_choice = [
        ('held', 'Проведен'),
        ('cancaled', 'Отмена'),
    ]
    
    payed_choice = [
        ('payed', 'Оплачен'),
        ('notpayed', 'Не оплачен'),
    ]
    
    date = models.DateField(auto_now_add=True)
    student = models.ManyToManyField(Student, verbose_name="Студент", related_name="student_related")
    teacher = models.ManyToManyField(Teacher, verbose_name="Преподаватель", related_name="teacher_related")
    status = models.CharField(max_length=15, choices=status_choice)
    payed = models.CharField(max_length=15, choices=payed_choice)
    reason = models.TextField(blank=True, null=True, verbose_name="Причина отмены")
    
