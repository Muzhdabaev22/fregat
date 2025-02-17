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


class StudentsCode(models.Model):
    code = models.CharField("Код ученика", max_length=50, unique=True)
    teacher = models.ManyToManyField(Teacher, verbose_name="Учитель", related_name="teacher_related_stud")
     
    def __str__(self):
        return self.code
        
class Student(models.Model):
    username = models.CharField("Логин", max_length=100, unique=True, default=None)
    name = models.CharField("Имя", max_length=100)
    surname = models.CharField("Фамилия", max_length=100)
    city = models.CharField("Город", max_length=100, null=True, blank=True)
    contacts = models.CharField("Контакты", max_length=100)
    
    code = models.ManyToManyField(StudentsCode, verbose_name="Код ученика", related_name="student_code")
    
    image = models.ImageField("Изображение", null=True, blank=True)
    start_point = models.TextField("Начальный уровень", null=True, blank=True)
    current_point = models.TextField("Сейчас", null=True, blank=True)
    
    def __str__(self):
        return f"{self.name}"
    
    
class Lessons(models.Model):
    
    payed_choice = [
        ('payed', 'Оплачен'),
        ('notpayed', 'Не оплачен'),
    ]
    
    date = models.DateField()
    student = models.ManyToManyField(Student, verbose_name="Студент", related_name="student_related")
    teacher = models.ManyToManyField(Teacher, verbose_name="Преподаватель", related_name="teacher_related")
    status = models.CharField(max_length=30)
    payed = models.CharField(max_length=15, choices=payed_choice)
    reason = models.TextField(blank=True, null=True, verbose_name="Причина отмены")
    
    
    
