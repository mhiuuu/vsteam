from django.shortcuts import render
from .models import Article


def resources(request):
    articles = Article.objects.all()
    recent_articles = Article.objects.all()[:3]
    context = {'articles' : Article}
    return render(request, "html/resources.html")


def display_article(request):
    articles = Article.objects.first()
    context = {'article' : articles}
    return render(request, "html/article.html", context)
