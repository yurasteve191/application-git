from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Orders)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('orderId', 'orderStatus', 'orderPayType', 'invoiceId', 'orderPosterCreateCheck', 'orderTransactionId', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('orderId', 'full_description')