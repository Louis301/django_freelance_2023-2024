from django.shortcuts import render
from .models import User
from django.http import HttpResponseRedirect

# Create your views here.

def auth_screen(request):
    if request.POST.get('auth_btn') != None:
        try:
            u = User.objects.get(name=request.POST.get('user_name'))
            return HttpResponseRedirect('main/') 
        except User.DoesNotExist:
            print('пользователь не найден')

    return render(request, 'authorization.html')


def reg_screen(request):
    if request.POST.get('reg_btn') != None:
        try:
            u = User.objects.get(name=request.POST.get('user_name'))
            print('пользователь в базе')
        except User.DoesNotExist:
            u = User()
            u.name = request.POST.get('user_name')
            u.save()
            return HttpResponseRedirect('/') 

    return render(request, 'registration.html')


def main(request):
    print('main')
    return render(request, 'registration.html')