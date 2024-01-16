from django import forms 
from App_Quizes.models import Quiz

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['subject', 'title', 'marks', 'questions']