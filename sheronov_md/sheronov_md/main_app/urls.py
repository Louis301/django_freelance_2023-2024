from django.urls import path
from . import views


urlpatterns = [
    path('', views.start, name='start'),
    path('delete_canvas/<int:canvas_id>', views.delete_canvas, name='delete_canvas'),
    path('main/<int:canvas_id>', views.main, name='main'),
]
