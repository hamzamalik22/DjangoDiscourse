from django.shortcuts import render,redirect
from django.db.models import Q
from .models import *
from .forms import *



# rooms = [
#     {'id' : 1 , 'name' : "Python here & there"},
#     {'id' : 2 , 'name' : "movies i can watch"},
#     {'id' : 3 , 'name' : "anime lovers"},
# ]



def home(request):
    q = request.GET.get('q')  if request.GET.get('q') != None else '' 

    rooms = Room.objects.filter(
        Q(topic__topic__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q) 
    )

    room_count = rooms.count()
    topics = Topic.objects.all()
    context = {'rooms' : rooms,'topics' : topics,'room_count' : room_count}
    return render(request,'chat/home.html',context)


def room(request,pk):
    room = Room.objects.get(id=pk)
    context = {'room' : room}
    return render(request,'chat/room.html',context)

def createRoom(request):
    form = RoomForm()
    if request.method ==  'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form' : form}
    return render(request,'chat/room_form.html',context)


def updateRoom(request,pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST,instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form' : form}
    return render(request,'chat/room_form.html',context)

def deleteRoom(request,pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    context = {'obj' : room}
    return render(request,'chat/delete.html',context)