from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', "price", "category", "available", 'updated', "discount"]
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'discount', 'available']
    prepopulated_fields = {'slug': ('name',)}


