from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('room/<str:pk>/',views.room,name="room"),

    path('create-room',views.createRoom,name="create-room"),
    path('update-room/<str:pk>/',views.updateRoom,name="update-room"),
    path('delete-room/<str:pk>/',views.deleteRoom,name="delete-room"),
    path('delete-message/<str:pk>/',views.deleteMessage,name="delete-message"),
    path('loginpage/',views.loginPage,name="loginpage"),
    path('registerpage/',views.registerPage,name="registerpage"),
    path('logout/',views.logoutPage,name="logout"),
    path('userprofile/<str:pk>',views.userProfile,name="userprofile"),
    path('update-user/',views.updateUser,name="update-user"),

]
