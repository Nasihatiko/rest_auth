from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Product(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='products')
    description = models.TextField(max_length=500, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    amount = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title
