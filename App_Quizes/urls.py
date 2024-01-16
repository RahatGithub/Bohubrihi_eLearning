from django.urls import path 
from App_Quizes import views 

app_name = "App_Quizes" 

urlpatterns = [
    path('home/', views.home, name="home"),
    path('new_quiz/', views.new_quiz, name="new_quiz"),
    path('quiz/<int:id>', views.quiz_view, name="quiz_view")
]