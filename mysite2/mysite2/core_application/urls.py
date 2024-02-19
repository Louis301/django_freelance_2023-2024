from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('send_form/', views.contacts_form_handler, name='form_handler')
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]