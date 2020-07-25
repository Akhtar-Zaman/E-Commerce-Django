from django.contrib import admin
from . models import Customer, Product, Order, OrderItem, ShippingAddress



class Customer_Admin(admin.ModelAdmin):
    model = Customer
    list_display = ['name', 'email']

class Product_Admin(admin.ModelAdmin):
    model = Product
    list_display = ['name', 'products_quantity', 'price', 'digital']

class Order_Admin(admin.ModelAdmin):
    model = Order
    list_display = ['customer', 'transaction_id', 'date_orderd', 'complete']

class OrderItem_Admin(admin.ModelAdmin):
    model = OrderItem
    list_display = ['product', 'order_quantity', 'date_orderd']

class ShippingAddress_Admin(admin.ModelAdmin):
    model = ShippingAddress
    list_display = ['customer', 'address', 'city', 'date_orderd']

admin.site.register(Customer, Customer_Admin )
admin.site.register(Product, Product_Admin )
admin.site.register(Order, Order_Admin )
admin.site.register(OrderItem, OrderItem_Admin )
admin.site.register(ShippingAddress, ShippingAddress_Admin )
