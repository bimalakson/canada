from django.shortcuts import render

# Create your views here.
def transaksi(request):
    context = {}
    return render(request, 'transaksi/transaksi.html', context)

def keranjang(request):
    context = {}
    return render(request, 'transaksi/keranjang.html', context)

def pembayaran(request):
    context = {}
    return render(request, 'transaksi/pembayaran.html', context)

