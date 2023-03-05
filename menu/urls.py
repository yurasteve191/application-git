from django.urls import path

from .views import *

urlpatterns = [
    path('createOrder/', create_order),
    path('createPosterOrder/', create_order_in_poster),
    path('deleteOrder/', delete_order),
    path('orderStatus/', order_status),
    path('payResult/', change_order_status),

    path('getMenuFromPoster', get_menu_from_poster)
]