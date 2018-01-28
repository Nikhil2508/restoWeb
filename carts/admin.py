from django.contrib import admin

# Register your models here.
from .models import Carts, CartItem

class CartItemInline(admin.TabularInline):
    model = CartItem

class CartAdmin(admin.ModelAdmin):
    inlines = [CartItemInline]
    class Meta:
        model = Carts


admin.site.register(Carts, CartAdmin)
