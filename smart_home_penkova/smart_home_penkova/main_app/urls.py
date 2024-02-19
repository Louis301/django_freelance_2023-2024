from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('rooms/', views.rooms, name='rooms'),
    path('rooms/<room>/', views.room_page, name='room_page'),
]