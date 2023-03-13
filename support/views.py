from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse
from .servises import *
from .models import *

@csrf_exempt
def contactMe(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        contact = Contacts(name=name, phone=phone)
        contact.save()
        return JsonResponse({'result': True})
    else:
        return JsonResponse({'result': False, 'message': 'Only POST requests are allowed'})

@csrf_exempt
def addFeedBack(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        desctiprion = request.POST.get('desctiprion')
        phone = request.POST.get('phone')
        rate = request.POST.get('rate')

        feedback = Feedback(name=name, phone=phone, desctiprion=desctiprion,rate=rate )
        feedback.save()
        
        return JsonResponse({'result': True})
    else:
        return JsonResponse({'result': False, 'message': 'Only POST requests are allowed'})
    
@csrf_exempt
def addRent(request):
    if request.method == 'POST':
        print('------------------')
        print(request.POST)
        type = request.POST.get('type')
        id = request.POST.get('id')
        name = request.POST.get('name')
        desctiprion = request.POST.get('desctiprion')
        phone = request.POST.get('phone')

        if(type == 'shelves'):
            shelves = RentingShelves(name=name, shelves_id=id, desctiprion=desctiprion, phone=phone)
            shelves.save()
            
        if(type == 'canvas'):
            canvas = RentingCanvas(name=name, shelves_id=id, desctiprion=desctiprion, phone=phone)
            canvas.save()

        return JsonResponse({'result': True})
    else:
        return JsonResponse({'result': False, 'message': 'Only POST requests are allowed'})

def getReserved(request):
    canvas_id = request.GET.get('canvas_id')
    shelves_id = request.GET.get('shelves_id')

    if canvas_id:
        # отримати зарезервовані дати для полотна з вказаним id
        reserved_dates = get_reserved_canvas(canvas_id)
        return JsonResponse({'reserved_dates': reserved_dates})
    elif shelves_id:
        # отримати зарезервовані дати для стелажа з вказаним id
        reserved_dates = get_reserved_shelves(shelves_id)
        return JsonResponse({'reserved_dates': reserved_dates})
    else:
        # якщо не вказано id полотна або стелажа, повернути порожній список
        return JsonResponse({'reserved_dates': []})