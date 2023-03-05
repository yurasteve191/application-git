from django.conf import settings
from random import randint
from .models import *
import json
import datetime
import requests

_token = settings.POSTER_TOKEN

def get_categories_from_poster():
    url = f'https://joinposter.com/api/menu.getCategories?token={_token}&fiscal=0'
    response = requests.get(url).json()['response']
    return response

def get_goods_from_poster():
    url = f'https://joinposter.com/api/menu.getProducts?token={_token}&fiscal=0'
    response = requests.get(url).json()['response']
    return response

def sent_new_check_to_monobank_pay_and_get_data(request):
    destination = request.POST.get('destination')
    amount = request.POST.get('amount')
    basketOrder = json.loads(request.POST.get('basketOrder'))
    redirectUrl = request.POST.get('redirectUrl')
    # Generate random orderId with 5 digits
    orderId = randint(10000, 99999)

    url = 'https://api.monobank.ua/api/merchant/invoice/create'
    headers = {
        "Content-Type": "application/json", 
        "X-Token": "u9Ae6ER_IPySY74IfQ0x_itBdlPOTC54VSap2ugn6RCs"
    }
    data = {
        "amount": int(amount),
        "ccy": 980,
        "merchantPaymInfo": {
            "reference": "84d0070ee4e44667b31371d8f8813947",
            "destination": destination,
            "basketOrder": basketOrder
        },
        "redirectUrl": redirectUrl,
        "webHookUrl": "https://example.com/mono/acquiring/webhook/maybesomegibberishuniquestringbutnotnecessarily",
        "validity": 3600,
        "paymentType": "debit",
        "qrId": ""
    }
    response = requests.post(url, headers=headers, json=data)
    # Create new order
    order = Orders(orderId=orderId, orderStatus='pay', orderPayType='monobank', invoiceId= response.json()['invoiceId'])
    order.save()
    return response.json()


def create_new_check_in_poster_and_get_data(request):
    url = f'https://joinposter.com/api/incomingOrders.createIncomingOrder?token={_token}'
    invoiceId = request.POST.get('invoceId')
    products = json.loads(request.POST.get('products'))
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "spot_id": int(1),
        "first_name":'Додаток "Інформатика"',
        "phone":'380977261682',
        "products": products,
        "promotion":[]
    }
    response = requests.post(url, headers=headers, json=data).json()
    order = Orders.objects.get(invoiceId=invoiceId)
    order.orderId = response['response']['incoming_order_id']
    order.created_at = response['response']['created_at']
    order.orderTransactionId = response['response']['transaction_id']
    order.orderStatus = 'waiting for approve'
    order.save()

    return response


def check_an_poster_order_by_id_and_get_status(orderId):
    url = f'https://joinposter.com/api/incomingOrders.getIncomingOrder?token={_token}&incoming_order_id={orderId}'
    response = requests.get(url).json()
    return response['response']['status']

def check_an_poster_check_by_order_transaction_id_and_get_the_status(transaction_id):
    # print(transaction_id)
    order = Orders.objects.get(orderTransactionId = transaction_id)
    create_at_date = order.created_at.split()[0]
    create_at_date_dt = datetime.datetime.strptime(create_at_date, '%Y-%m-%d')

    current_date_dt = create_at_date_dt + datetime.timedelta(days=1)
    current_date = current_date_dt.strftime('%Y-%m-%d')

    url = f'https://joinposter.com/api/transactions.getTransactions?token={_token}&date_from={create_at_date}&date_to={current_date}'

    response = requests.get(url).json()
    # print(response['response']['data'])
    # Шукаємо транзакцію з потрібним transaction_id
    order_transaction = None
    for transaction in response['response']['data']:
        if transaction['transaction_id'] == order.orderTransactionId:
            order_transaction = transaction
            break
    
    pay_type = None
    try:
        pay_type = order_transaction['pay_type']
    except:pass
    
    return pay_type


def get_poster_order_transaction_id(orderId):
    url = f'https://joinposter.com/api/incomingOrders.getIncomingOrder?token={_token}&incoming_order_id={orderId}'
    response = requests.get(url).json()
    return response['response']['transaction_id']

