from django.shortcuts import render
from .models import Category, Dish
from django.http import HttpResponseRedirect


def show_menu(request, category_title=None):
    categories = Category.objects.all()
    selected_category = categories[0].title if category_title == None else category_title
    dishes = Dish.objects.filter(category=selected_category, in_shopping_cart=False, in_order_list=False)
    context = { 
        'categories' : categories[:3],
        'selected_category' : selected_category,
        'dishes' : dishes,
    }
    return render(request, 'menu.html', context=context)


def add_to_cart(request, dish_id: int):
    dish = Dish.objects.get(id=dish_id)
    dish.in_shopping_cart = True
    dish.save()
    return HttpResponseRedirect(f'/{dish.category}/')


def show_cart(request):
    dishes = Dish.objects.filter(in_shopping_cart=True)
    context = {
        'dishes' : dishes,
    }
    return render(request, 'cart.html', context=context)    


def decrement_dish_quantity(request, dish_id: int):
    dish = Dish.objects.get(id=dish_id)
    
    if dish.quantity > 1:
        dish.quantity -= 1
    
    dish.save()
    return HttpResponseRedirect('/cart/')


def increment_dish_quantity(request, dish_id: int):
    dish = Dish.objects.get(id=dish_id)
    dish.quantity += 1
    dish.save()
    return HttpResponseRedirect('/cart/')


def make_order(request, dish_id=None):
    if dish_id == None:
        dishes = Dish.objects.filter(in_shopping_cart=True, for_an_order=True)
        for dish in dishes:
            dish.in_shopping_cart = False
            dish.for_an_order = False
            dish.in_order_list = True
            dish.save()
    else:
        dish = Dish.objects.get(id=dish_id)
        dish.in_shopping_cart = False
        dish.for_an_order = False
        dish.in_order_list = True
        dish.save()

    return HttpResponseRedirect('/cart/')


def mark_for_order(request, dish_id: int):
    dish = Dish.objects.get(id=dish_id)

    if dish.for_an_order:
        dish.for_an_order = False
    else:
        dish.for_an_order = True

    dish.save()
    return HttpResponseRedirect('/cart/')


def remove_from_cart(request, dish_id: int):
    dish = Dish.objects.get(id=dish_id)
    dish.in_shopping_cart = False
    dish.for_an_order = False
    dish.quantity = 1
    dish.save()
    return HttpResponseRedirect('/cart/')


def show_orders(request):
    dishes = Dish.objects.filter(in_order_list=True)
    total_price = total_quantity = 0

    for dish in dishes:
        total_price += dish.price
        total_quantity += dish.quantity

    context = {
        'dishes' : dishes,
        'total_price' : total_price,
        'total_quantity' : total_quantity,
    }
    return render(request, 'orders.html', context=context)    


def cancel_order(request):
    dishes = Dish.objects.filter(in_order_list=True)

    for dish in dishes:
        dish.in_order_list = False
        dish.save()
    
    return HttpResponseRedirect('/orders/')
