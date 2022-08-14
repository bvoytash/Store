from django.urls import path

from Store.Store_api.views import ProductListView, SingleProductView, OrderListView, EditOrderView, StatsListView

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product list'),
    path('products/<int:pk>', SingleProductView.as_view(), name = 'single product'),
    path('orders/', OrderListView.as_view(), name='orders list'),
    path('orders/<int:pk>', EditOrderView.as_view(), name='edit order'),
    path('stats/', StatsListView.as_view(), name='stats')
]