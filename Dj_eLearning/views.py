from django.shortcuts import render, HttpResponseRedirect, HttpResponse


def home(request):
    return HttpResponse("Universal home page")