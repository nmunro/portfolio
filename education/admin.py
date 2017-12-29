from django.contrib import admin

from .models import Education, Qualification


admin.site.register(Qualification)
admin.site.register(Education)
