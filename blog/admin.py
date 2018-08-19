from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Post, Project, Blog


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class BlogTextAdmin(SummernoteModelAdmin): 
    summernote_fields = '__all__'

class ProjectTextAdmin(SummernoteModelAdmin): 
    summernote_fields = '__all__'

admin.site.register(Post)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Blog, BlogTextAdmin)
