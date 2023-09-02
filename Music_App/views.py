from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

def Index(request) :
    context = {
        'fav' : Album.objects.all(),
        'special' : Album.objects.filter(special = True)
    }
    return render(request , 'pages/index.html' , context)

def Favorites(request) :
    context = {
        'fav' : Album.objects.filter(favorite=True)
    }
    return render(request , 'pages/favorites.html',context)

def Contact(request) :
    if request.method == 'POST' :
        add_feedback = ContactForm(request.POST)
        if add_feedback.is_valid() :
            add_feedback.save()
    context = {
        'form' : ContactForm()
    } 
    return render(request , 'pages/contact.html' , context)

def Single_Page(request,id) :
    
    album_id = Album.objects.get(id = id)
    context = {
        'album' : album_id
    }
    return render(request , 'pages/singlepage.html', context )

def Specials(request) :
    context = {
        'special' : Album.objects.filter(special = True)
    }
    return render(request , 'pages/specials.html' , context)

def Artists(request) :
    context = {
        'artist' :Artist.objects.all()
    }
    return render(request , 'pages/artists.html' ,context)

