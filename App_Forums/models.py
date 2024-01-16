from django.db import models
from django.contrib.auth.models import User 

class Forum(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='forums_created')
    topic = models.CharField(max_length=264, blank=True)
    created_date = models.DateField(auto_now_add=True) 

    class Meta:
        ordering = ['-created_date',]
    
    def __str__(self):
        return f"{self.topic}({self.created_date})"


class Question(models.Model):
    asked_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions_asked')
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE, related_name='questions')
    question = models.TextField(blank=True)
    image = models.ImageField(upload_to='forum_pics', blank=True)
    created_date = models.DateField(auto_now_add=True) 

    class Meta: 
        ordering = ['-created_date',]
    
    def __str__(self):
        # return f"{{self.question|slice:':50' }}"
        return self.question 
    


class Answer(models.Model):
    answered_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answers_given')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='questions')
    answer = models.TextField(blank=True)
    created_date = models.DateField(auto_now_add=True) 

    class Meta: 
        ordering = ['-created_date',]

    def __str__(self):
        return self.answer