from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'price', 'quantity', 'image_show', 'categories')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description')

    def image_show(self, obj):
        if obj.images:
            return mark_safe("<img src='{}' width='60' />".format(obj.images.url))
        return "None"

    image_show.__name__ = 'Картинка'

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug')
    list_display_links = ('id', 'title')
    search_fields = ('title',)

admin.site.register(Products, ProductsAdmin)
admin.site.register(OrderItems)
admin.site.register(Orders)
admin.site.register(Users)
admin.site.register(Categories, CategoriesAdmin)

