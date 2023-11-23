from django.shortcuts import render
from .models import *



# rooms = [
#     {'id' : 1 , 'name' : "Python here & there"},
#     {'id' : 2 , 'name' : "movies i can watch"},
#     {'id' : 3 , 'name' : "anime lovers"},
# ]



def home(request):
    rooms = Room.objects.all()
    context = {'rooms' : rooms}
    return render(request,'chat/home.html',context)


def room(request,pk):
    room = Room.objects.get(id=pk)
    context = {'room' : room}
    return render(request,'chat/room.html',context)