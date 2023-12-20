from django.contrib import admin
from .models import PostBlog, Movie, Accent, Author, Topic, Level, Episode

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ('title',)}


class UrlCinemaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ('title',)}


admin.site.register(PostBlog, PostAdmin)
admin.site.register(Movie)
admin.site.register(Episode, UrlCinemaAdmin)
admin.site.register(Accent)
admin.site.register(Author)
admin.site.register(Level)
admin.site.register(Topic)
