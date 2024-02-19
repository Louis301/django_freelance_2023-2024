from django.shortcuts import render
from .models import Problem

# Create your views here.

def delete_problem(problem_id):
    p = Problem.objects.get(id=int(problem_id))
    p.delete()
    

def create_problem(wording):
    if wording != '':
        p = Problem()
        p.wording = wording
        p.save()


def main_screen(request):
    if request.POST.get('delete_btn') != None:
        delete_problem(request.POST.get('delete_btn'))

    if request.POST.get('create_btn') != None:
        create_problem(request.POST.get('new_problem'))

    context = {'all_problems' : Problem.objects.all()}

    return render(request, 'main_app/main.html', context=context)
