from django import forms 
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User 
from App_Accounts.models import UserProfile

class CreateNewUser(UserCreationForm):
    email = forms.EmailField(required=True, label="", widget=forms.TextInput(attrs={'placeholder':'Email'}))
    username = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password1 = forms.CharField(
        required = True, 
        label = "",
        widget = forms.PasswordInput(attrs={'placeholder':'Password'})
    )
    password2 = forms.CharField(
        required = True, 
        label = "",
        widget = forms.PasswordInput(attrs={'placeholder':'Confirm password'})
    )
    profile_pic = forms.ImageField(
        required=False,
        label="Profile Picture",
        widget=forms.ClearableFileInput(attrs={'accept': 'image/*'}),
    )
    TYPE_CHOICES = [ ('Teacher', 'Teacher'), ('Student', 'Student') ]
    type = forms.ChoiceField(
        choices=TYPE_CHOICES,
        widget=forms.RadioSelect,
        required=True,
        label="User Type",
        initial=['Student']
    )

    class Meta:
        model = User 
        fields = ('email', 'username', 'password1', 'password2', 'profile_pic', 'type')