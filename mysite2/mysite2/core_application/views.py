from django.shortcuts import render
from .models import ContactsForm

def index_view(request):
    template_name = 'core_application/index.html'
    return render( request, template_name )


def contacts_form_handler(request):
    template_name = 'core_application/send_form.html'

    if request.POST.get('send_form') == 'Отправить заявку':
        ContactsForm.objects.create(
            fullname = request.POST.get('fullname'),
            phone_number = request.POST.get('phone_number'),
            mail= request.POST.get('mail'),
            message= request.POST.get('message')
        )

    return render( request, template_name )