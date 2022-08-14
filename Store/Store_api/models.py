from django.db import models
from django.core import validators


class Product(models.Model):
    TITLE_MAX_LENGTH = 30
    PRICE_MIN_VALUE = 0.01

    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    price = models.DecimalField(max_digits=4, decimal_places=2,
        validators=(
            validators.MinValueValidator(PRICE_MIN_VALUE),
        )
    )

    def __str__(self):
        return self.title


class Order(models.Model):
    date_order = models.DateField()
    products = models.ManyToManyField(Product, related_name='products')
