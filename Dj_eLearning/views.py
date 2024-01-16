from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from App_Articles.models import Article 
from App_Quizes .models import Quiz 
from App_Forums.models import Forum  


def home(request):
    num_of_articles = Article.objects.all().count()
    num_of_quizes = Quiz.objects.all().count()
    num_of_forums = Forum.objects.all().count() 
    
    context = {
        'title' : 'Home', 
        'num_of_articles' : num_of_articles,
        'num_of_quizes' : num_of_quizes, 
        'num_of_forums' : num_of_forums
    }
    return render(request, 'home.html', context)