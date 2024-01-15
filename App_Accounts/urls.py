from django.urls import path 
from App_Accounts import views 

app_name = "App_Accounts" 

urlpatterns = [
    path('signup/', views.sign_up, name='sign_up'), 
    path('login/', views.log_in, name='log_in'),
    path('logout/', views.logout_user, name='logout'), 
    # path('profile/<int:user_id>/', views.profile, name='profile'),
]