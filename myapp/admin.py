from django.contrib import admin
from .models import Restaurant, MenuItem, MenuItemVariant, Category, Order, OrderItem


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['name', 'cuisine_type', 'rating', 'delivery_time', 'delivery_fee', 'is_promoted', 'is_active']
    list_filter = ['is_promoted', 'is_active', 'cuisine_type']
    search_fields = ['name', 'cuisine_type', 'description']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['is_promoted', 'is_active']


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'restaurant', 'category', 'price', 'is_popular', 'is_available']
    list_filter = ['restaurant', 'category', 'is_vegetarian', 'is_spicy', 'is_popular', 'is_available']
    search_fields = ['name', 'description', 'restaurant__name']
    list_editable = ['price', 'is_popular', 'is_available']


@admin.register(MenuItemVariant)
class MenuItemVariantAdmin(admin.ModelAdmin):
    list_display = ['menu_item', 'name', 'price']
    list_filter = ['menu_item__restaurant']
    search_fields = ['menu_item__name', 'name']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'icon']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'restaurant', 'customer_name', 'status', 'total', 'created_at']
    list_filter = ['status', 'created_at', 'restaurant']
    search_fields = ['order_id', 'customer_name', 'customer_email', 'customer_phone']
    readonly_fields = ['order_id', 'created_at', 'updated_at']
    date_hierarchy = 'created_at'


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'menu_item', 'variant_name', 'quantity', 'price', 'subtotal']
    list_filter = ['order__restaurant', 'order__created_at']
    search_fields = ['order__order_id', 'menu_item__name']
