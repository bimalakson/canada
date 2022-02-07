from django.shortcuts import render
from .models import *

# Create your views here.
def transaksi(request):
    products    = Product.objects.all()
    context     = {'products':products}
    return render(request, 'transaksi/transaksi.html', context)

def keranjang(request):
    
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items =  order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}

    context = {'items':items, 'order':order}
    return render(request, 'transaksi/keranjang.html', context)

def pembayaran(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items =  order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}

    context = {'items':items, 'order':order}
    return render(request, 'transaksi/pembayaran.html', context)

