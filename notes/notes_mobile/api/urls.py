from django.urls import path
from . import views


urlpatterns = [
    path('', name='getRoutes', view=views.getRoutes),
    path('notes/', name='getNotes', view=views.getNotes),
    path('notes/create/', name='createNote', view=views.createNote),
    path('notes/<str:pk>/update/', name='updateNote', view=views.updateNote),
    # path('notes/update/', name='updateNote', view=views.updateNote),
    path('notes/<str:pk>/delete/', name='deleteNote', view=views.deleteNote),
    path('notes/<str:pk>', name='getNote', view=views.getNote),
]
