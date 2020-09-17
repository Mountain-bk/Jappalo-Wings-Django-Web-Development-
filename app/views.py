from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    return render(request, 'index.html')

def menu(request):
    return render(request, 'menu.html')

def store_finder(request):
    return render(request, 'store-finder.html')

def order_type(request):
    return render(request, 'order-type.html')

def delivery(request):
    return render(request, 'delivery.html')

def pick_up(request):
    return render(request, 'pick-up.html')

def payment(request):
    return render(request, 'payment.html')

def order_confirmed(request):
    return render(request, 'confirmation.html')
