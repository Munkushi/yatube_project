from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.


#Главная страница
def index(request):
    return HttpResponse('Главная страница')



#Страница сообществ
def group_posts(request, slug):
    return HttpResponse(f'Сообщество {slug}')


