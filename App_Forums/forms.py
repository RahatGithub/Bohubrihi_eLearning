from django import forms 
from App_Forums.models import Forum, Question, Answer

class ForumForm(forms.ModelForm):
    class Meta:
        model = Forum
        fields = ['topic']


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question', 'image']


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['answer']
        widgets = {
            'answer': forms.Textarea(attrs={'rows': 2}), 
        }