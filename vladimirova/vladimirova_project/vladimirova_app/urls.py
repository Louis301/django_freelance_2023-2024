from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('new_account/', views.create_account, name='new_account'),
    path('plan/<int:account_id>/', views.plan, name='plan'),
    path('new_task/<int:account_id>/', views.create_task, name='new_task'),
    path('close_task/<int:task_id>/', views.close_task, name='close_task'),
    path('remove_task/<int:task_id>/', views.remove_task, name='remove_task'),
]
