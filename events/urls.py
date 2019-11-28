from django.urls import path

from . import views

urlpatterns = [
    path('', views.view_events, name='view_events'),
    path('concerts/', views.view_concerts, name='view_concerts'),
    path('sports/', views.view_sports, name='view_sports'),
    path('other/', views.view_other, name='view_other'),
    path('signup/', views.signup, name='signup'),
]