from django.urls import path

from .views import *

urlpatterns = [
    path('contackMe/', contactMe),
    path('addFeedback/', addFeedBack),
    path('addRent/', addRent),
    path('getReserved/', getReserved)
]