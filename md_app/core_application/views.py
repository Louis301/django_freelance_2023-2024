from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Profile, Product
import json


def save_account_info(user_id: int) -> None:
    with open('account_info.json', 'w', encoding='utf-8') as fout:
        json.dump({ 'current_account_id' : user_id }, fout)


def get_current_account_id() -> int:
    with open('account_info.json', 'r', encoding='utf-8') as fin:
        json_data = json.load(fin)
        return json_data.get('current_account_id')


def coalesce(value, alt_value):
    return alt_value if (value is None) else value


def show_main(request, prod_id=None):    
    products = Product.objects.filter(profile_id=get_current_account_id())
    if not prod_id is None:        
        p = Product.objects.get(id=prod_id)        
        p.in_cart = not p.in_cart
        p.save()    
    context = { 'products' : products[:3] }
    return render(request, 'core_application/main.html', context)


def show_about(request):
    return render(request, 'core_application/about.html') 


def show_authorize(request):
    msg = ''
    login = coalesce(request.POST.get('login'), '')
    password = coalesce(request.POST.get('password'), '')
    if request.POST.get('btn_entering') != None:
        try:
            cur_profile = Profile.objects.get(login=login, password=password)
            save_account_info(cur_profile.id)
            return HttpResponseRedirect('main/') 
        except Profile.DoesNotExist:
            msg = 'некорректный ввод'
    context = { 'msg' : msg, 'login' : login, 'password' : password }
    return render(request, 'core_application/authorize.html', context)


def show_registration(request):
    msg = ''
    login = coalesce(request.POST.get('login'), '')
    password = coalesce(request.POST.get('password'), '')
    fio = coalesce(request.POST.get('fio'), '')
    phone = coalesce(request.POST.get('phone'), '')
    email = coalesce(request.POST.get('email'), '')
    delivery_address = coalesce(request.POST.get('delivery_address'), '')
    if request.POST.get('btn_registration') != None:
        cur_profile = Profile.objects.filter(login=login, password=password)
        if cur_profile.count() == 0:
            Profile.objects.create(login=login, password=password,fio=fio,phone=phone,email=email, delivery_address=delivery_address  )
            return HttpResponseRedirect('/')
        else:
            msg = 'пользователь существует'
    context = { 'msg' : msg,'fio' : fio,'phone' : phone,'email' : email,'delivery_address' : delivery_address,'login' : login,'password' : password}
    return render(request, 'core_application/registration.html', context)


def show_profile(request):
    msg = ''
    cur_profile = Profile.objects.get(id=get_current_account_id())
    if request.POST.get('btn_save') != None:
        if Profile.objects.filter(login=request.POST.get('login'), password=request.POST.get('password')).count() != 0 and (request.POST.get('login') != cur_profile.login and request.POST.get('password') != cur_profile.password):
            msg = 'пользователь существует'
        else:
            cur_profile.login = request.POST.get('login')
            cur_profile.password = request.POST.get('password')
            cur_profile.fio = request.POST.get('fio')
            cur_profile.phone = request.POST.get('phone')
            cur_profile.email = request.POST.get('email')
            cur_profile.delivery_address = request.POST.get('delivery_address')
            cur_profile.save()
            return HttpResponseRedirect('/profile')
    context = { 'msg' : msg, 'fio' : cur_profile.fio, 'phone' : cur_profile.phone, 'email' : cur_profile.email, 'delivery_address' : cur_profile.delivery_address, 'login' : cur_profile.login, 'password' : cur_profile.password }
    return render(request, 'core_application/profile.html', context)


def show_catalog(request):
    return render(request, 'core_application/catalog.html'
    # , context
    )


def show_cart(request):
    products = Product.objects.filter(profile_id=get_current_account_id(), in_cart=True)
    context = {
        'products' : products
    }
    return render(request, 'core_application/cart.html', context)
