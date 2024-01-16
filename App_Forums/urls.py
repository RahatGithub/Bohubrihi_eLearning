from django.urls import path 
from App_Forums import views 

app_name = "App_Forums" 

urlpatterns = [
    path('home/', views.home, name="home"),
    path('new_forum/', views.new_forum, name="new_forum"),
    path('<int:id>', views.forum_view, name="forum_view"),
    path('new_question/<int:id>', views.new_question, name="new_question"),
    path('questions/<int:id>', views.question_view, name="question_view"),
]