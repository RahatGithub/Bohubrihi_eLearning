from django import forms 
from App_Articles.models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article 
        fields = ['caption', 'description', 'image']