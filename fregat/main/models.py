from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse


class PostBlog(models.Model):
    title = models.CharField(max_length=100)
    url = models.SlugField()
    text = RichTextUploadingField()
    img = models.ImageField()
    
    def __str__(self):
        return self.title

class Accent(models.Model):
    accent = models.CharField("Имя", max_length=100)
   
    
    def __str__(self):
        return self.accent
    
    class Meta:
        verbose_name = "Акцент"
        verbose_name_plural = "Акценты"

class Topic(models.Model):
    topic = models.CharField("Имя", max_length=100)
    
    def __str__(self):
        return self.topic
    
    class Meta:
        verbose_name = "Тема"
        verbose_name_plural = "Темы"

class Level(models.Model):
    level = models.CharField("Уровень", max_length=10)
    
    def __str__(self):
        return self.level
    
    class Meta:
        verbose_name = "Уровень"
        verbose_name_plural = "Уровни"
        
class Author(models.Model):
    name = models.CharField("Имя", max_length=100)
    url = models.URLField("Ссылка на страницу")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

class Episode(models.Model):
    title = models.CharField("Название", max_length=100, unique=True)
    number_epis = models.PositiveSmallIntegerField("Номер эпизода")
    url = models.SlugField("Ссылка")
    level = models.ManyToManyField(Level, verbose_name="Уровень", related_name="lvl_related")
    accent = models.ManyToManyField(Accent, verbose_name="Акцент", related_name="accent_related")
    topic = models.ManyToManyField(Topic, verbose_name="Тема", related_name="topic_related")
    author = models.ManyToManyField(Author, verbose_name="Автор", related_name="author_related")
    video = models.FileField("Видео", max_length=100)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Эпизод"
        verbose_name_plural = "Эпизоды"
        
class Movie(models.Model):
    title = models.CharField("Название фильма", max_length=100)
    img = models.ImageField("Изображение")
    episodes = models.ManyToManyField(Episode, verbose_name="Эпизод", related_name="ep_related")
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"
    