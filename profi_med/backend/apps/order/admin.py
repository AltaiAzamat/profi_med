from .models import *
from django.contrib import admin



@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['name','image','created','updated']
    prepopulated_fields = {'name':('image',)}