from django.shortcuts import render, HttpResponseRedirect, HttpResponse


def home(request):
    return render(request, 'home.html')