from django.urls import path

from .views import *

urlpatterns = [
    path('createOrder/', create_order),
    path('createPosterOrder/', create_order_in_poster),
    path('orderStatus/', order_status),

    path('getMenuFromPoster', get_menu_from_poster)
]