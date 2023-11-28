from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class PostBlog(models.Model):
    title = models.CharField(max_length=30)
    url = models.SlugField()
    text = RichTextUploadingField()
    img = models.ImageField()
    
    def __str__(self):
        return self.title
    
    
