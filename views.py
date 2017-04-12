from django.http import HttpResponse
from django.shortcuts import render
from .models import Album

def index(request):
    all_albums = Album.objects.all()
    context = {'all_albums': all_albums}
    return render(request, 'music/index.html', context)

def index(request):
    all_albums = Album.objects.all()
    context = {'all_albums': all_albums}
    return render(request, 'sing/text.html', context)



def detail(request, album_id):
    return HttpResponse("<h2>details for album_id: " +str(album_id) + "</h2>")

