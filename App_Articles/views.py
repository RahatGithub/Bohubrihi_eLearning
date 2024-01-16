from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from App_Articles.models import Article
from App_Articles.forms import ArticleForm

def home(request):
    articles = Article.objects.all()
    context = {'articles' : articles}
    return render(request, 'App_Articles/home.html', context)


def new_article(request):
    form = ArticleForm()
    
    context = {'form':form}
    return render(request, 'App_Articles/new_article.html', context)