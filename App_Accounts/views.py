from django.shortcuts import render, HttpResponseRedirect
from App_Accounts.forms import CreateNewUser
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy 
from App_Accounts.models import UserProfile
from django.contrib.auth.models import User 


def sign_up(request):
    form = CreateNewUser()
    # registered = False 
    if request.method == 'POST':
        form = CreateNewUser(data=request.POST, files=request.FILES)
        if form.is_valid():
            user = form.save()
            # registered = True 
            type = form.cleaned_data['type']
            profile_pic = form.cleaned_data['profile_pic']
            user_profile = UserProfile(user=user, type=type, profile_pic=profile_pic)
            user_profile.save()
            return HttpResponseRedirect(reverse('App_Accounts:log_in'))
    
    return render(request, 'App_Accounts/signup.html', 
                  context={
                      'title':'Sign up', 
                      'form' : form
                    })

def log_in(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None: 
                login(request, user)
                # return HttpResponseRedirect(reverse(''))
                return render(request, 'home.html') 
    
    return render(request, 'App_Accounts/login.html', context={'title':'Login', 'form':form})


@login_required 
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('App_Accounts:log_in'))