from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ['title','anons','image','full_text','date']
    prepopulated_fields = {'anons':('date',)}