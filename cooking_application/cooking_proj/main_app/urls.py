from django.urls import path
from . import views


urlpatterns = [
    path('', views.show_menu, name='menu_path'), 
    path('cart/', views.show_cart, name='cart_path'),
    path('orders/', views.show_orders, name='orders_path'),
    path('make_order/', views.make_order, name='make_order'),
    path('cancel_order/', views.cancel_order, name='cancel_order'),
    path('<category_title>/', views.show_menu, name='menu_path'),
    path('add_to_cart/<int:dish_id>/', views.add_to_cart, name='add_to_cart'),
    path('increment_dish_quantity/<int:dish_id>', views.increment_dish_quantity, name='increment_dish_quantity'),
    path('decrement_dish_quantity/<int:dish_id>', views.decrement_dish_quantity, name='decrement_dish_quantity'),
    path('make_order/<int:dish_id>/', views.make_order, name='make_order'),    
    path('mark_for_order/<int:dish_id>', views.mark_for_order, name='mark_for_order'),
    path('remove_from_cart/<int:dish_id>', views.remove_from_cart, name='remove_from_cart'),
]
