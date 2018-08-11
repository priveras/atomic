from django.contrib import admin

from .models import Post, Project, Blog


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post)
admin.site.register(Project)
admin.site.register(Blog, BlogAdmin)
