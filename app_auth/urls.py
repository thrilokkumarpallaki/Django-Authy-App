from django.urls import path
from . import views

app_name = 'authy'

urlpatterns = [
    path('index', views.index, name='index'),
    path('login', views.user_login, name='login'),
    path('signup', views.user_signup, name='signup'),
    path('logout', views.user_logout, name='logout'),
    path('home/<user>', views.home, name='home'),
    path('home/<user>/profile', views.profile_settings, name='user_profile_settings'),
]
