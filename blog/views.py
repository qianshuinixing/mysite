from django.shortcuts import render
from .models import Article
# Create your views here.


def titles(request):
    articles = Article.objects.all()
    return render(request, 'blog/titles.html', {'blogs':articles})


def article(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'blog/content.html', {"article":article})