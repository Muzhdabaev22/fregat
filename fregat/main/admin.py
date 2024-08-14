from django.contrib import admin
from .models import PostBlog, Movie, Accent, Author, Topic, Level, Episode, Vocabulary, TestCinema, DiscusBoard, SubStory

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ('title',)}

class VocabularyAdminInline(admin.TabularInline):
    model = Vocabulary
    extra = 0


class TestAdminInline(admin.TabularInline):
    model = TestCinema
    extra = 0
    
class DiscusAdminInline(admin.TabularInline):
    model = DiscusBoard
    extra = 0

class SubStoryAdminInline(admin.TabularInline):
    model = SubStory
    extra = 0
    
class EpisodeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ('title',)}
    list_display = [field.name for field in Episode._meta.fields]
    inlines = [VocabularyAdminInline, TestAdminInline, DiscusAdminInline, SubStoryAdminInline]
    
    class Meta:
        model = Episode
    


admin.site.register(PostBlog, PostAdmin)
admin.site.register(Movie)
admin.site.register(Episode, EpisodeAdmin)
admin.site.register(Accent)
admin.site.register(Author)
admin.site.register(Level)
admin.site.register(Topic)

