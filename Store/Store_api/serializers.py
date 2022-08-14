from rest_framework import serializers
from Store.Store_api.models import Product, Order
from rest_framework.fields import SerializerMethodField


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True,
                                 style={'base_template': 'input.html'})

    class Meta:
        model = Order
        fields = ('id', 'date_order', 'products')


class StatsSerializer(serializers.ModelSerializer):
    value = serializers.IntegerField(source='products.count', read_only=True)
    price = serializers.SerializerMethodField()

    def get_price(self, obj):
        price = 0
        for product in obj.products.all():
            price += product.price
        return f'{price:.2f}'

    class Meta:
        model = Order
        fields = ('id', 'date_order', 'value', 'price')
