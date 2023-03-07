from django.http import JsonResponse
from .serializers import OrdersSerializer
from django.views.decorators.csrf import csrf_exempt
from .models import Orders
import json

from .servises import *

@csrf_exempt
def order_status(request):
    if request.method == 'POST':
        orders_json = request.POST.get('orders')
        invoice_ids = json.loads(orders_json)
        orders = Orders.objects.filter(invoiceId__in=invoice_ids)
        for order in orders:
            if order.orderStatus == 'pay':
                pay_result = check_the_order_for_pay_done_in_monobanl(order.invoiceId)
                if pay_result['status'] == 'success':
                    order = Orders.objects.get(orderId=order.orderId)
                    order.orderStatus = 'prepearing'
                    order.save()

            if order.orderStatus == 'waiting for approve':
                if check_an_poster_order_by_id_and_get_status(order.orderId) == 1:
                    order = Orders.objects.get(orderId=order.orderId)
                    #отримує orderTransactionId
                    transactionId = get_poster_order_transaction_id(order.orderId)
                    order.orderTransactionId = transactionId
                    order.orderStatus = 'approved'
                    order.save()
                
            if order.orderStatus == 'approved':
                pay_type = check_an_poster_check_by_order_transaction_id_and_get_the_status(order.orderTransactionId)
                if pay_type == 0 or pay_type == 1 or pay_type == 2 or pay_type == 3:
                    order = Orders.objects.get(orderId=order.orderId)
                    order.delete()
                
        serializer = OrdersSerializer(orders, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def create_order(request):
    if request.method == 'POST':
        type = request.POST.get('type')
        payData = None

        if(type == 'monobank'):
            payData = sent_new_check_to_monobank_pay_and_get_data(request)
            # print(payData)
            return JsonResponse({'response': payData})
        
        if(type == 'cripto'):
            payData = False
            return JsonResponse({'response': payData})
        
        else:
            return JsonResponse({'response': False})
      
@csrf_exempt  
def create_order_in_poster(request):
    payData = create_new_check_in_poster_and_get_data(request)
    return JsonResponse({'response': payData})

#
def get_menu_from_poster(request):
    if request.method == 'GET':
        _categories = get_categories_from_poster()
        _goods = get_goods_from_poster()
        return JsonResponse({'categories': _categories, 'goods': _goods})
    
    if request.method == 'POST':
        return JsonResponse({'fuck': 'you'})
