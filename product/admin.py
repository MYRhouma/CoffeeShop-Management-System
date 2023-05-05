from django.contrib import admin
from .models import Category, Product

class SlugAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Category,SlugAdmin)
admin.site.register(Product,SlugAdmin)
