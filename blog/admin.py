from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Post, Project, Blog


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

class BlogTextAdmin(SummernoteModelAdmin): 
    summernote_fields = '__all__'

admin.site.register(Post)
admin.site.register(Project)
admin.site.register(Blog, BlogTextAdmin)
