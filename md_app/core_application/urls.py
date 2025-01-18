from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index_view, name='index'),
    # path('send_form/', views.contacts_form_handler, name='form_handler')
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),

    path('', views.show_authorize, name='authorize'),
    path('main/<int:prod_id>/', views.show_main, name='main'),
    path('main/', views.show_main, name='main'),
    path('registration/', views.show_registration, name='registration'),
    path('profile/', views.show_profile, name='profile'),
    path('catalog/', views.show_catalog, name='catalog'),
    path('cart/', views.show_cart, name='cart'),
    path('about/', views.show_about, name='about')
    # main             
    # registration     
    # authorize      ''
    # profile
    # catalog
    # cart
    # about
]