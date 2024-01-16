from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from App_Forums.models import Forum, Question, Answer
from App_Forums.forms import ForumForm, QuestionForm, AnswerForm

def home(request):
    forums = Forum.objects.all()
    context = {'forums' : forums, 'title' : 'Forums'}
    return render(request, 'App_Forums/home.html', context)


def forum_view(request, id):
    forum = Forum.objects.get(id=id)
    questions = Question.objects.filter(forum=forum)
    
    context = {
        'questions' : questions,
        'forum' : forum
    }
    return render(request, 'App_Forums/forum.html', context)


def question_view(request, id):
    question = Question.objects.get(id=id)
    answers = Answer.objects.filter(question=question)
    form = AnswerForm()
    if request.method == 'POST':
        form = AnswerForm(data=request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.answered_by = request.user
            answer.question = question 
            answer.save()
            url = reverse('App_Forums:question_view', kwargs={'id': id})
            return HttpResponseRedirect(url)
    context = {
        'title' : f"Q.{question.question}",
        'question' : question,
        'answers' : answers,
        'form' : form
    }
    return render(request, 'App_Forums/question.html', context)



def new_forum(request):
    form = ForumForm()
    if request.method == 'POST':
        form = ForumForm(data=request.POST)
        if form.is_valid():
            forum = form.save(commit=False)
            forum.creator = request.user 
            forum.save()
            return HttpResponseRedirect(reverse('App_Forums:home'))
    context = {'form':form}
    return render(request, 'App_Forums/new_forum.html', context)



def new_question(request, id):
    form = QuestionForm()
    forum = Forum.objects.get(id=id)
    if request.method == 'POST':
        form = QuestionForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            question = form.save(commit=False)
            question.asked_by = request.user 
            question.forum = forum 
            question.save()
            url = reverse('App_Forums:new_question', kwargs={'id': id})
            return HttpResponseRedirect(url)
    context = {
        'form' : form, 
        'forum' : forum
    }
    return render(request, 'App_Forums/new_question.html', context)