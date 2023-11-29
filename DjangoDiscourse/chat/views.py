from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.decorators import login_required
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

    chats = Message.objects.all().order_by('-created')

    context = {'rooms' : rooms,'topics' : topics,'room_count' : room_count,'chats': chats,'page' : 'Django Discourse'}
    return render(request,'chat/home.html',context)


def room(request,pk):
    room = Room.objects.get(id=pk)
    chats = room.message_set.all().order_by('-created')

    participants = room.participants.all()

    if request.method == 'POST':
        message = Message.objects.create(
            user = request.user,
            room = room,
            message = request.POST.get('message_body')
        )
        room.participants.add(request.user)
        return redirect('room',pk = room.id)

    context = {'room' : room,'page' : room.name,'chats':chats,'participants': participants}
    return render(request,'chat/room.html',context)


@login_required(login_url='loginpage')
def createRoom(request):
    form = RoomForm()
    topics = Topic.objects.all()
    if request.method ==  'POST':
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name = topic_name)

        Room.objects.create(
            host = request.user,
            topic = topic ,
            name = request.POST.get('name'),
            description = request.POST.get('description'),

        )


        # form = RoomForm(request.POST)
        # if form.is_valid():
        #     room = form.save(commit=False)
        #     room.host = request.user
        #     room.save()

        return redirect('home')
    context = {'form' : form,'page' : 'Create Room','topics' : topics}
    return render(request,'chat/room_form.html',context)


@login_required(login_url='loginpage')
def updateRoom(request,pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    topics = Topic.objects.all()

    if  request.user != room.host:
        messages.error(request,"Only Room Owner can edit!")
        return redirect('home')

    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name = topic_name)
        room.name = request.POST.get('name')
        room.topic = topic
        room.description = request.POST.get('description')
        room.save()
        return redirect('home')

    context = {'form' : form,'page' : 'Update Room','topics' : topics,'room' : room}
    return render(request,'chat/room_form.html',context)


@login_required(login_url='loginpage')
def deleteRoom(request,pk):
    room = Room.objects.get(id=pk)

    if  request.user != room.host:
        messages.error(request,"Only Room Owner can edit!")
        return redirect('home')

    if request.method == 'POST':
        room.delete()
        return redirect('home')
    context = {'obj' : room,'page' : 'Delete Room'}
    return render(request,'chat/delete.html',context)

@login_required(login_url='loginpage')
def deleteMessage(request,pk):
    message = Message.objects.get(id=pk)

    if  request.user != message.user:
        messages.error(request,"Only Owner can edit!")
        return redirect('room')

    if request.method == 'POST':
        message.delete()
        return redirect('home')
    context = {'obj' : message,'page' : 'Delete Message'}
    return render(request,'chat/delete.html',context)


def loginPage(request):


    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username = username)
        except: 
            messages.error(request,'User dont exists..')
            return redirect('loginpage')
    
        user = authenticate(request,username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Username or Password incorrect')

    context = {'page' : 'Login'}
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

    context = {'page' : 'Register'}
    return render(request,'chat/register.html',context)

def logoutPage(request):
    logout(request)
    return redirect('home')


def userProfile(request,pk):
    user = User.objects.get(id=pk)
    rooms = user.room_set.all()
    chats = user.message_set.all()
    topics = Topic.objects.all()
    context = {'user' : user,'rooms' : rooms,'chats' : chats,'topics' : topics}
    return render(request,'chat/profile.html',context)


@login_required(login_url='login')
def updateUser(request):
    user = request.user
    form = UserForm(instance=user)

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user-profile', pk=user.id)

    return render(request, 'chat/update_user.html', {'form': form})