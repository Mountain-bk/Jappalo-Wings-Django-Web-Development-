from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home-page'),
    path('menu', views.menu, name='menu'),
    path('store-finder', views.store_finder, name='store-finder'),
    path('order-type', views.order_type, name='order-type'),
    path('delivery', views.delivery, name='delivery'),
    path('pick-up', views.pick_up, name='pick-up'),
    path('payment', views.payment, name='payment'),
    path('confirmation', views.order_confirmed, name='confirmation')
]
