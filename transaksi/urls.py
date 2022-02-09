from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('transaksi/', views.transaksi, name="transaksi"),
    path('keranjang/', views.keranjang, name="keranjang"),
    path('pembayaran/', views.pembayaran, name="pembayaran"),
    path('produk/', views.produk, name="produk"),

    path('update_item/', views.updateItem, name="update_item"),
    path('create_product/', views.createProduct, name="create-product"),
    path('process_order/', views.processOrder, name="process_order")
]