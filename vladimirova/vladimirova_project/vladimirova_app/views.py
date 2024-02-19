from django.shortcuts import render
from .models import Account, Task
from django.http import HttpResponseRedirect


def index(request):
    msg = ''

    if request.POST.get('auth_btn') != None:
        m = request.POST.get('field_mail')
        p = request.POST.get('field_password')

        if Account.objects.filter(mail=m, password=p).count() > 0:
            return HttpResponseRedirect(f'plan/{Account.objects.get(mail=m, password=p).id}/') 
        else:
            msg = 'аккаунт не найден'

    return render(request, 'savvinova_app/index.html', { 'msg' : msg })


def create_account(request):
    msg_danger = ''
    msg_success = ''
    context = {}

    if request.POST.get('reg_btn') != None:
        m = request.POST.get('field_mail')
        p = request.POST.get('field_password')
        pr = request.POST.get('field_password_repeat')
        n = request.POST.get('field_name')
        aa = request.POST.get('agreement_accept')

        if aa != None:
            if p != pr:
                msg_danger = 'пароли не совпадают' 
            else:
                if Account.objects.filter(mail=m, password=p).count() > 0:
                    msg_danger = 'аккаунт уже есть' 
                else:
                    Account.objects.create(mail=m, password=p, name=n)
                    msg_success = 'аккаунт создан'
        else:
            msg_danger = 'вы не дали согласие' 

        context = { 'm' : m, 'p' : p, 'pr' : pr, 'n' : n, 'aa' : aa, 'msg_danger' : msg_danger, 'msg_success' : msg_success }

    return render(request, 'savvinova_app/new_account.html', context=context)


def plan(request, account_id):
    account = Account.objects.get(id=account_id)

    context = {
        'account' : account, 
        'active_tasks' : Task.objects.filter(account_id=account_id, closed=False), 
        'closed_tasks' : Task.objects.filter(account_id=account_id, closed=True), 
    }
    
    return render(request, 'savvinova_app/plan.html', context=context)


def create_task(request, account_id):
    account = Account.objects.get(id=account_id)
    msg_success = ''
    msg_danger = ''

    if request.POST.get('task_create_btn') != None:
        ts = request.POST.get('parent_task')
        ftb = request.POST.get('field_task_body')
        fd = request.POST.get('field_deadline')

        if Task.objects.filter(body=ftb).count() == 0:
            Task.objects.create( deadline=fd, body=ftb, parent_task=ts, account_id=account_id )
            msg_success = 'создана задача'
        else:
            msg_danger = 'задача уже поставлена'

    context = { 'account' : account, 'parent_tasks' : Task.objects.filter(account_id=account_id), 'msg_success' : msg_success, "msg_danger" : msg_danger }
    
    return render(request, 'savvinova_app/new_task.html', context=context)


def close_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.closed = True
    task.save()
    return HttpResponseRedirect(f'/plan/{task.account_id}/')


def remove_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return HttpResponseRedirect(f'/plan/{task.account_id}/')
