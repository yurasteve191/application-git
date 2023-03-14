from django.urls import path

from .views import *

urlpatterns = [
    path('getNews/', getNews),
    path('getTopNews/', getTopNews),
    path('getMusics/', getMusics),
    path('getActions/', getActions),
    path('getQRCode/', createQrCode),
]