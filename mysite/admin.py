from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Directory)
class DirectoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'directory']
    
@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'file', 'directory']