from django.urls import path 
from App_Articles import views 

app_name = "App_Articles" 

urlpatterns = [
    path('home/', views.home, name="home"),
    path('new_article/', views.new_article, name="new_article"),
]