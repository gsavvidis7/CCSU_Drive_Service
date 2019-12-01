from django.urls import path

from . import views

urlpatterns = [
    path('', views.view_events, name='view_events'),
    path('concerts/', views.view_concerts, name='view_concerts'),
    path('sports/', views.view_sports, name='view_sports'),
    path('other/', views.view_other, name='view_other'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.view_profile, name='profile'),
    path('profile/driver/', views.view_driver_profile, name='view_driver_profile'),
    path('profile/rider/', views.view_rider_profile, name='view_rider_profile'),
    path('profile/driver/remove', views.remove_driver_entry, name='remove_driver_entry'),
    path('profile/rider/remove', views.remove_rider_entry, name='remove_rider_entry'),
]