from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse
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