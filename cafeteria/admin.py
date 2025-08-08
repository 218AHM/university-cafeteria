from django.contrib import admin
from .models import Category, FoodItem, Order, OrderItem


# Categories
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_id', 'category_name')


# Inline OrderItem inside Order
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0  # no empty fields
    readonly_fields = ('subtotal',)


# Food Items
@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    list_display = ('food_name', 'food_price', 'category', 'is_available')
    list_filter = ('category', 'is_available')
    search_fields = ('food_name',)
    list_editable = ('is_available',)


# Orders
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'customer_name', 'order_status', 'timestamp', 'total_amount')
    list_filter = ('order_status',)
    inlines = [OrderItemInline]
    readonly_fields = ('timestamp', 'total_amount')


class OrderAdmin(admin.ModelAdmin):
    list_display = ("order_id", "customer_name", "customer_id", "order_status", "timestamp", "total_amount")
    list_filter = ("order_status", "timestamp")
    search_fields = ("customer_name", "customer_id")