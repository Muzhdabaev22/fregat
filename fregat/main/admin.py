from django.contrib import admin
from .models import PostBlog

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ('title',)}


admin.site.register(PostBlog, PostAdmin)
