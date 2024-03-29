from django.shortcuts import render
from .models import Article


def resources(request):
    articles = Article.objects.all()
    main_post = Article.objects.first()
    recent_articles = Article.objects.all()[:3]
    context = {
        "main_post" : main_post,
        "recent_articles" : recent_articles,
    }
    return render(request, "html/resources.html", context)


def display_article(request):
    articles = Article.objects.first()
    context = {'article' : articles}
    return render(request, "html/article.html", context)
