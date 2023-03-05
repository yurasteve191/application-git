from django.shortcuts import render
from django.http import JsonResponse
from .models import News, TopNews
from .serializers import NewsSerializer, TopNewsSerializer

def getNews(request):
    if request.method == 'GET':
        queryset = News.objects.all()
        serializer = NewsSerializer(queryset, many=True)
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
    