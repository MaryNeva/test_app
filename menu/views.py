from django.shortcuts import render, HttpResponse

# Create your views here.
from .models import MainCategory, Category


def menu(request):
    menus = MainCategory.objects.all()
    return render(request, "menu/menu.html", {"menu": menus})


def main_category(request, main_slug):
    menus = MainCategory.objects.get(slug=main_slug)
    return HttpResponse("Category:" + menus.name)


def sub_category(request, main_slug, sub_slug):
    menus = MainCategory.objects.get(slug=main_slug)
    return HttpResponse("Category:" + menus.name + ". Sub_category:" + menus.sub.get(slug=sub_slug).name)
