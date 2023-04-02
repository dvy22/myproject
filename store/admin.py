from django.contrib import admin
from store.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display= ('name','slug')
    prepopulated_fields= {'slug':('name',)}
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display= ('title','author','slug','price','in_stock','created_at','updated')
    list_filter= ('in_stock','in_active')
    list_editable= ('price','in_stock')
    prepopulated_fields={'slug':('title',)}