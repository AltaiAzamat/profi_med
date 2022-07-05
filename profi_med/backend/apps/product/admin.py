from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','slug','id']
    prepopulated_fields = {'slug':('name',)}


@admin.register(SubCategory)
class SubCategory(admin.ModelAdmin):
    list_display = ('name','category','slug','id')
    list_filter = ('category',)
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('id','name')





@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'price',
        'image',
        'category',
        'subcategory',
        'created',
        'updated',
        'is_active'
    ]
    #
    # @admin.register(BanerImage)
    # class BanerImageAmin(admin.ModelAdmin):
    #     list_display = ['name','add_link','image','created']
    #     list_filter = ['created']