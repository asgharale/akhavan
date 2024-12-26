from django.db import models


class Cards(models.Model):
    pass

class CardItem(models.Model):
    product = models.ForeignKey("store.Product", on_delete=models.CASCADE, blank=False, null=False)

class Order(models.Model):
    STATUS_CHOICES = (
        ('I', "In Progress"),
        ('C', "Canceled")
    )
    status = models.CharField(choices=STATUS_CHOICES, max_length=1, default='C')

class OrderItem(models.Model):
    product = models.ForeignKey("store.Product", on_delete=models.CASCADE, blank=False, null=False)