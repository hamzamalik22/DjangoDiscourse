from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
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


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get('username')
        except: 
            messages.error(request,'User dont exists..')
            return redirect('loginpage')
    
        user = authenticate(request,username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Username or Password incorrect')

    context = {}
    return render(request,'chat/login.html',context)

def registerPage(request):
    if request.method == 'POST':
        first_name = request.POST.get("first_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = User.objects.filter(username = username)
         
        if user.exists():
            messages.error(request,"User already exists")
            return redirect('/login')

        user = User.objects.create(
            first_name = first_name , 
            username = username , 
            email = email , 
        )

        user.set_password(password)
        user.save()
        messages.success(request,'Account Created Successfully')
        return redirect('loginpage')

    context = {}
    return render(request,'chat/register.html',context)

def logoutPage(request):
    logout(request)
    return redirect('home')