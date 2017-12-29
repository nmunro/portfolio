from django.contrib import admin

from .models import Proverb


class ProverbAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('content',)}

admin.site.register(Proverb, ProverbAdmin)
