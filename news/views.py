from django.shortcuts import get_object_or_404, redirect, render

from news.forms import CreateCategoryModelForm, CreateNewsModelForm
from news.models import Category, News


def home(request):
    news_list = News.objects.all()
    return render(request, "home.html", {"news_list": news_list})


def news_details(request, id):
    news = get_object_or_404(News, pk=id)
    return render(request, "news_details.html", {"news": news})


def categories(request):
    form = CreateCategoryModelForm()
    if request.method == "POST":
        form = CreateCategoryModelForm(request.POST)
        if form.is_valid():
            # form.save()
            Category.objects.create(**form.cleaned_data)
            return redirect("home-page")
    return render(request, "categories_form.html", {"form": form})


def news(request):
    form = CreateNewsModelForm()
    if request.method == "POST":
        form = CreateNewsModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("entrou aqui")
            return redirect("home-page")
    return render(request, "news_form.html", {"form": form})
