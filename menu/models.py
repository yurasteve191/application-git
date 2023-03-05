from django.db import models

class Orders(models.Model):
    orderId = models.IntegerField()
    orderStatus = models.CharField(max_length=255)
    invoiceId = models.CharField(max_length=255)
    orderPayType = models.CharField(max_length=255)
    orderPosterCreateCheck = models.BooleanField(default=False)
    orderTransactionId = models.IntegerField(default=0, blank=True, null=True)

    created_at = models.CharField(max_length=255)
