from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginpg, name='loginpg'),
    path('index/', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
]