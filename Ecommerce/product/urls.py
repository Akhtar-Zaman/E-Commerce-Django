
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('product_details/', views.product_details, name='product_details'),
    path('product_cart/', views.product_cart, name='product_cart'),
    path('update_item/', views.updateItem, name='update_item'),
]
