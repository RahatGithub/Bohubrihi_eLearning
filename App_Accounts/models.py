from django.db import models
from django.contrib.auth.models import User 


class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('Teacher', 'Teacher'),
        ('Student', 'Student'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=None)
    full_name = models.CharField(max_length=264, blank=True)
    dob = models.DateField(blank=True, null=True) 

    def __str__(self):
        return f"{self.user}" 