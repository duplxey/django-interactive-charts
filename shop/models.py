from django.db import models
from django.utils import timezone


class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    price = models.FloatField(default=0)

    def __str__(self):
        return f'{self.name} (${self.price})'


class Purchase(models.Model):
    customer_full_name = models.CharField(max_length=64)
    item = models.ForeignKey(to=Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    PAYMENT_METHODS = [
        ('CC', 'Credit card'),
        ('DC', 'Debit card'),
        ('ET', 'Ethereum'),
        ('BC', 'Bitcoin'),
    ]
    payment_method = models.CharField(max_length=2, default='CC', choices=PAYMENT_METHODS)
    time = models.DateTimeField(auto_now_add=False)
    successful = models.BooleanField(default=False)

    class Meta:
        ordering = ['-time']

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.pk is None:
            self.time = timezone.now()

        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return f'{self.customer_full_name}, {self.payment_method} ({self.quantity}x {self.item.name})'
