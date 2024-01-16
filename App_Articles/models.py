from django.db import models
from django.contrib.auth.models import User 


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='article')
    image = models.ImageField(upload_to='article_pics')
    caption = models.CharField(max_length=264, blank=True) 
    description = models.TextField(blank=True) 
    upload_date = models.DateField(auto_now_add=True)

    class Meta: 
        ordering = ['-upload_date',]
    
    def __str__(self):
        return self.caption 