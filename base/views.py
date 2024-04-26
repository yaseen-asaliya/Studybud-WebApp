from django.shortcuts import render

# Create your views here.

rooms = [
    {'id': 1, 'name': 'Let us play Fortnite'},
    {'id': 2, 'name': 'Let us play GTA V'},
    {'id': 3, 'name': 'Let us play Valorant'},
]

def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html' , context)

def room(request, pk):
    room = None
    for r in rooms:
        if r['id'] == int(pk):
            room = r
    
    context = {'room':room}
    return render(request, 'base/room.html', context)

