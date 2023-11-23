from django.shortcuts import render



rooms = [
    {'id' : 1 , 'name' : "Python here & there"},
    {'id' : 2 , 'name' : "movies i can watch"},
    {'id' : 3 , 'name' : "anime lovers"},
]



def home(request):
    context = {'rooms' : rooms}
    return render(request,'chat/home.html',context)


def room(request,pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room' : room,'page' : f'{i["name"]}'.upper()}
    return render(request,'chat/room.html',context)