from django.contrib import admin
from .models import Contacts, Feedback, RentingCanvas, RentingShelves


@admin.register(Contacts)
class ContatsAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'comentar', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'phone')

@admin.register(Feedback)
class FeedbacksAdmin(admin.ModelAdmin):
    list_display = ('name', 'desctiprion', 'phone', 'rate', 'comentar', 'created_at')
    list_filter = ('created_at', 'rate',)
    search_fields = ('name', 'phone', 'rate')

@admin.register(RentingShelves)
class RentingShelvesAdmin(admin.ModelAdmin):
    list_display = ('name', 'desctiprion', 'phone', 'rate', 'comentar', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'phone', 'rate')

@admin.register(RentingCanvas)
class RentingCanvasAdmin(admin.ModelAdmin):
    list_display = ('name', 'desctiprion', 'phone', 'rate', 'comentar', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'phone', 'rate')

