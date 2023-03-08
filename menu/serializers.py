from django.core import serializers
from rest_framework import serializers
from .models import Orders

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ['orderId', 'invoiceId' , 'orderStatus', 'created_at']