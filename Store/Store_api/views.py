from django.db.models import Count
from rest_framework import generics as api_views


from Store.Store_api.models import Product, Order
from Store.Store_api.serializers import ProductSerializer, OrderSerializer, StatsSerializer


class ProductListView(api_views.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class SingleProductView(api_views.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderListView(api_views.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class EditOrderView(api_views.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class StatsListView(api_views.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = StatsSerializer

    def get_queryset(self):
        date_start = self.request.query_params.get('date_start')
        date_end = self.request.query_params.get('date_end')
        metric = self.request.query_params.get('metric')
        # if metric == "price":  TODO if metric si price/value
        # return
        queryset = Order.objects.annotate(value=(Count('products')))
        queryset = queryset.filter(date_order__range=(date_start, date_end))
        return queryset