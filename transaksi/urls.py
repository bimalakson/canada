from django.urls import path
from . import views

urlpatterns = [
    path('transaksi/', views.transaksi, name="transaksi"),
    path('keranjang/', views.keranjang, name="keranjang"),
    path('pembayaran/', views.pembayaran, name="pembayaran"),
]