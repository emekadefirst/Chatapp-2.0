from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.home, name='home'),
    path('message', views.chat, name='chat'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
]