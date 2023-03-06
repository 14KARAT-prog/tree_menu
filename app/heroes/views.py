from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.template.loader import render_to_string
from django.shortcuts import redirect, render

from .models import *

menu = ["menu", "menu", "menu"]

def index(request):
    posts = Heroes.objects.all()
    return render(request, 'heroes/index.html', {'posts': posts,'menu': menu,'title': 'Главная страница'})

def about(request):
    return render(request, 'heroes/about.html', {'menu': menu,'title': 'О сайте'})


def category(request, catid):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1>Категории</h1><p>{catid}</p>")

def archive(request, year):
    if int(year) > 2023:
        return redirect('home', permanent=True)
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')



def treeMenu(request):
    items = Item.objects.filter(parent__isnull=True)
    return render(request, 'heroes/tree_menu.html', {'tags': items})