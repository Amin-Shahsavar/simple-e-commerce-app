from django.contrib import admin
from store.models import Product, Collection, Customer, Cart, CartItem, Order, OrderItem


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'description', 'unit_price', 'inventory', 'last_update', 'collection']


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'featured_product']


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name','email', 'phone', 'birth_date', 'membership']


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['created_at']