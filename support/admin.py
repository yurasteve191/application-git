from django.contrib import admin
from .models import Contacts, Feedback, RentingCanvas, RentingShelves, CanvasRentedDates, ShelvesRentedDates


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
    list_display = ('shelves_id', 'name', 'desctiprion', 'phone', 'comentar', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'phone')

@admin.register(RentingCanvas)
class RentingCanvasAdmin(admin.ModelAdmin):
    list_display = ('canvas_id', 'name', 'desctiprion', 'phone', 'comentar', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'phone')

@admin.register(CanvasRentedDates)
class CanvasRentedDatesAdmin(admin.ModelAdmin):
    list_display = ('canvas_id', 'name', 'phone', 'date_from', 'date_to', 'comentar', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'phone')

@admin.register(ShelvesRentedDates)
class ShelvesRentedDatesAdmin(admin.ModelAdmin):
    list_display = ('shelves_id', 'name', 'phone', 'date_from', 'date_to', 'comentar', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'phone')

