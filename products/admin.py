from django.contrib import admin
from models import Products, Variation, ProductImage, Category, ProductFeatured
# Register your models here.


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0
    max_num = 10


class VariationInline(admin.TabularInline):
    model = Variation
    extra = 0

class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__','price']
    inlines = [
        VariationInline,
        ProductImageInline,
    ]
    class Meta:
        model = Products

admin.site.register(Products, ProductAdmin)
admin.site.register(ProductFeatured)
admin.site.register(Category)
admin.site.register(ProductImage)
admin.site.register(Variation)
