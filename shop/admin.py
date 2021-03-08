from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'available', 'added_on', 'updated_on', )
    list_filter = ('name', 'category', 'added_on',)
    prepopulated_fields = {'slug': ('name',)}