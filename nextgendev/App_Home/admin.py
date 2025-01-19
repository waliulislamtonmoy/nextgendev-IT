from django.contrib import admin

# Register your models here.

from .models import Home

class HomeAdmin(admin.ModelAdmin):
    list_display=['title','created_at']

admin.site.register(Home,HomeAdmin)