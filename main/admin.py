from django.contrib import admin

from main.models import Dish, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category',)
    list_filter = ('name', 'description', 'category',)
