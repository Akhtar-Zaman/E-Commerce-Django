
from . models import Customer, Product, Order, OrderItem, ShippingAddress
from django.shortcuts import render
from django.http import JsonResponse
import json




def index(request):
    product = Product.objects.all()
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    cartItems = order.get_cart_items
    return render (request, 'index.html', {'product':product, 'cartItems':cartItems})


def product_details(request):
    return render (request, 'a.html')


def product_cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = OrderItem.objects.all()
        cartItems = order.get_cart_items
        
        tax = 0.05 * order.get_cart_total
        shipping_cost = 15.0
        total= order.get_cart_total + tax + shipping_cost
    else:
        items=[]
        order=[]
        total=0
        tax=0
        shipping_cost=0
        cartItems =[]
        

    return render (request, 'cart.html', {'items': items,
                                          'order': order,
                                          'total': total,
                                          'tax': tax,
                                          'shipping_cost':shipping_cost,
                                          'cartItems':cartItems})


def updateItem(request):
   
    data = json.loads(request.body)
    
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('productId:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
 
    if action=='add':
        orderItem.order_quantity= (orderItem.order_quantity+1)

    elif action== 'remove':
        orderItem.order_quantity= (orderItem.order_quantity-1)

    orderItem.save()

    if orderItem.order_quantity<=0:
        orderItem.delete()


    return JsonResponse ("ITEM was added", safe=False)