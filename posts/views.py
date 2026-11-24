from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime



def hello_world_view(request):
    if request.method == "GET":
        return HttpResponse('привет это мой первый проект на django')


def about_me_view(request):
    if request.method == "GET":
        return HttpResponse('привет меня зовут бекназар мне 16 лет я бэкенд деволопер')






def favorite_writer(request):
    if request.method == "GET":
        return HttpResponse('мои любимые писатели Кормак Маккарти и Говард Лавкрафт')





def datetime_view(request):
    if request.method == "GET":
        now = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        return HttpResponse(f"Текущее время: {now}")