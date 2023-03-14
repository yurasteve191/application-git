from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import News, TopNews, Actions, Music
from .serializers import NewsSerializer, TopNewsSerializer, ActionsSerializer, MusicSerializer
from .servises import *

def getNews(request):
    if request.method == 'GET':
        queryset = News.objects.all()
        serializer = NewsSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        return JsonResponse({'result':False})
    
def getMusics(request):
    if request.method == 'GET':
        queryset = Music.objects.all()
        serializer = MusicSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        return JsonResponse({'result':False})
def getActions(request):
    if request.method == 'GET':
        queryset = Actions.objects.all()
        serializer = ActionsSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        return JsonResponse({'result':False})
    

def getTopNews(request):
    if request.method == 'GET':
        queryset = TopNews.objects.all()
        serializer = TopNewsSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        return JsonResponse({'result':False})

@csrf_exempt
def createQrCode(request):
    qrStrData = request.POST.get('qrStrData')
    readyCodeLink = createQR(qrStrData)
    return JsonResponse({'imageUrl':readyCodeLink})
    
    