from django.contrib import admin
from .models import Blog, Tag


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Tag)
admin.site.register(Blog, BlogAdmin)
