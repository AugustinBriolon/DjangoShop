from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    fields = ['image', 'name', 'quantity', 'price']

admin.site.register(Product)
