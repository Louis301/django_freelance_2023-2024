from django.shortcuts import render
from main_app.form import TrackForm
from main_app.models import Track


def start(request):
    if request.method == 'POST':
        form = TrackForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            context = {'form' : form, 'tracks' : Track.objects.all()}        
            return render(request, 'main_app/start.html', context)

    context = {'form' : TrackForm(), 'tracks' : Track.objects.all()}

    return render(request, 'main_app/start.html', context)

