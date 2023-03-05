from django.urls import path

from .views import *

urlpatterns = [
    path('getNews/', getNews),
    path('getTopNews/', getTopNews),
]