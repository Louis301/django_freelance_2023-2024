from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import NoteSerializer
from .models import Note
from django.shortcuts import render
from django.http import HttpResponseRedirect


@api_view(['GET'])
def getRoutes(request):
    # routes = [
    #     {
    #         'Endpoint' : '/notes/',
    #         'method' : 'GET',
    #         'body' : None,
    #         'description' : 'Returns an array of notes'
    #     },
    #     {
    #         'Endpoint' : '/notes/id',
    #         'method' : 'GET',
    #         'body' : None,
    #         'description' : 'Returns single note'
    #     },
    #     {
    #         'Endpoint' : '/notes/create/',
    #         'method' : 'POST',
    #         'body' : {'body': ""},
    #         'description' : 'Creates a note based on the received data'
    #     },
    #     {
    #         'Endpoint' : '/notes/id/delete/',
    #         'method' : 'DELETE',
    #         'body' : None,
    #         'description' : 'Deletes the note'
    #     }
    # ]
    return render(request, 'index.html', context={'notes' : Note.objects.all().order_by('-id')}) 


@api_view(['GET'])
def getNotes(request):
    # notes = Note.objects.all()
    # serializer = NoteSerializer(notes, many=True)
    # return Response(serializer.data)

    return render(request, 'index.html', context={'notes' : Note.objects.all()}) 


@api_view(['GET'])
def getNote(request, pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)


# @api_view(['POST'])
def createNote(request):
    # data = request.data

    # note = Note.objects.create(
    Note.objects.create(
        body=''
    )
    # serializer = NoteSerializer(note, many=False)
    # return Response(serializer.data)
    # return render(request, 'index.html', context={'notes' : Note.objects.all()}) 
    return HttpResponseRedirect('/') 


# @api_view(['PUT'])
def updateNote(request, pk):

    data = request.POST

    if data['send'] == 'сохранить':
        note = Note.objects.get(id=pk)
        note.body = data['note']
        note.save()
        return HttpResponseRedirect('/') 
    # note = Note.objects.get(id=pk)
    # serializer = NoteSerializer(note, data=request.data)

    # if serializer.is_valid():
    #     serializer.save()

    # return Response(serializer.data)


    return render(request, 'index.html', context={'notes' : Note.objects.all()}) 
 

# @api_view(['DELETE'])
def deleteNote(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()
    # return Response("Note was deleted!")
    # return render(request, 'index.html', context={'notes' : Note.objects.all()}) 
    return HttpResponseRedirect('/') 
