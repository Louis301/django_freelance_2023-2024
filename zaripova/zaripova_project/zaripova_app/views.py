from django.shortcuts import render
from .models import NotePhoto


def main(request):
    return render(request, 'main.html')


def adding(request):
    if request.POST.get('add_note') == 'Сохранить':

        NotePhoto.objects.create(
            title        = request.POST.get('photo_title'), 
            category     = request.POST.get('photo_category'), 
            comment      = request.POST.get('photo_comment'), 
            photo        = request.POST.get('photo_ref')
        )

    return render(request, 'adding.html')


def photos(request):

    all_photos = NotePhoto.objects.all()

    context = {
        'all_photos' : all_photos
    }

    return render(request, 'notes.html', context)

