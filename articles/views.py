from django.shortcuts import render
from .models import Article
# Create your views here.

def detail_article(request, pk):
    article = Article.objects.get(pk=pk)
    ctx = {
        'article' : article
    }
    return render(request, 'detail.html', ctx)

def list_article(request):
    articles = Article.objects.all()
    ctx = {
        'articles': articles
    }
    return render(request, 'list.html', ctx)