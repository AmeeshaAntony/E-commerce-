
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns = [
    path('cart', views.show_cart,name="cart"),
    path('add_to_cart', views.add_to_cart,name="add_to_cart"),
    path('remove_from_cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout_cart', views.checkout_cart, name='checkout_cart'),
    path('orders', views.show_orders, name='orders'),
]

