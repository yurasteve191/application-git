from django.contrib import admin
from .models import Contacts,Feedback


@admin.register(Contacts)
class ContatsAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'phone')

@admin.register(Feedback)
class FeedbacksAdmin(admin.ModelAdmin):
    list_display = ('name', 'desctiprion', 'phone', 'rate', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'phone', 'rate')