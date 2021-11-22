from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post
from .models import Group

# Create your views here.


#Главная страница
def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    title = 'Последние новости'
    context = {
        'title':title,
        'text':'Это главная страница проекта Yatube',
        'posts':posts,
    }
    return render(request, 'posts/index.html', context)

#template = ('index.html/') return render(request, template, {})

#Страница сообществ
def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    # Функция get_object_or_404 получает по заданным критериям объект 
    # из базы данных или возвращает сообщение об ошибке, если объект не найден.
    # В нашем случае в переменную group будут переданы объекты модели Group,
    # поле slug у которых соответствует значению slug в запросе
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    title = 'Список сообществ'
    context = {
        'title':title,
        'text':'Здесь будет информация о группах проекта Yatube',
        'group':group,
        'posts':posts,
    }
    return render(request, 'posts/group_list.html', context)
    #return HttpResponse(f'Сообщество {slug}')


