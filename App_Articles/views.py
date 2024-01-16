from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from App_Articles.models import Article
from App_Articles.forms import ArticleForm

def home(request):
    articles = Article.objects.all()
    context = {'articles' : articles}
    return render(request, 'App_Articles/home.html', context)


def new_article(request):
    form = ArticleForm()
    if request.method == 'POST':
        form = ArticleForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user 
            article.save()
            return HttpResponseRedirect(reverse('App_Articles:home'))
    context = {'form':form}
    return render(request, 'App_Articles/new_article.html', context)



def article_view(request, id):
    article = Article.objects.get(id=id)
    context = {'article' : article}
    return render(request, 'App_Articles/article.html', context)