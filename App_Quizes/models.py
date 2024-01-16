from django.db import models
from django.contrib.auth.models import User 


class Quiz(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quiz')
    subject = models.CharField(max_length=264, blank=True)
    title = models.CharField(max_length=264, blank=True) 
    marks = models.IntegerField(blank=True) 
    questions = models.TextField(blank=True) 
    upload_date = models.DateField(auto_now_add=True)

    class Meta: 
        ordering = ['-upload_date']
    
    def __str__(self):
        return self.title