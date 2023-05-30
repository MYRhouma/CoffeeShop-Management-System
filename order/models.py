from django.db import models
from django.db import models
from django.contrib.auth.models import User
from product.models import Product
from table.models import Table
from core.models import Business,Account
class Order(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE,null=True)
    table = models.ForeignKey(Table, null=True,on_delete=models.DO_NOTHING)
    STATUS_CHOICES = (
        (0, "En attente d'acceptation"),
        (1, 'En cours de préparation'),
        (2, 'Envoyé et en attente de paiement'),
        (3, 'Paiement effectué'),
    )
    user = models.ForeignKey(Account, related_name='orders', blank=True, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    address = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    place = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)

    paid = models.BooleanField(default=False)
    paid_amount = models.FloatField(blank=True, null=True)
    discount = models.FloatField(default=0.0)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    class Meta:
        ordering = ('-created_at',)

    def get_total_price(self):
        if self.paid_amount:
            return self.paid_amount / 1000
        return 0

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    price = models.FloatField()
    discount = models.FloatField(default=0.0)
    quantity = models.IntegerField(default=1)
    ready = models.BooleanField(default=False)

    def get_total_price(self):
        return self.price*self.quantity
