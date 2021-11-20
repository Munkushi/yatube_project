from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.


#Главная страница
def index(request):
    title = 'Последние новости'
    context = {
        'title':title,
        'text':'Это главная страница проекта Yatube'
    }
    return render(request, 'posts/index.html', {}, context)

#template = ('index.html/') return render(request, template, {})

#Страница сообществ
def group_posts(request):
    sec_title = 'Список сообществ'
    sec_context = {
        'title':sec_title,
        'text':'Здесь будет информация о группах проекта Yatube'
    }
    return render(request, 'posts/group_list.html', {}, sec_context)
    #return HttpResponse(f'Сообщество {slug}')


