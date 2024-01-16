from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse 
from App_Quizes.models import Quiz 
from App_Quizes.forms import QuizForm

def home(request):
    quizes = Quiz.objects.all()
    context = {'quizes' : quizes}
    return render(request, 'App_Quizes/home.html', context)


def new_quiz(request):
    form = QuizForm()
    if request.method == 'POST':
        form = QuizForm(data=request.POST)
        if form.is_valid():
            quiz = form.save(commit=False)
            quiz.teacher = request.user 
            quiz.save()
            return HttpResponseRedirect(reverse('App_Quizes:home'))
    context = {'form':form}
    return render(request, 'App_Quizes/new_quiz.html', context)


def quiz_view(request, id):
    quiz = Quiz.objects.get(id=id)
    context = {'quiz':quiz}
    return render(request, 'App_Quizes/quiz.html', context) 