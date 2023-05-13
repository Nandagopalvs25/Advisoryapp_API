from django.shortcuts import render
from rest_framework import generics
from base.models import CustomUser
from .serializers import ListUserSerializer,UserProfileSerializer
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.

class UserView(generics.ListAPIView):
    queryset= CustomUser.objects.all()
    serializer_class= ListUserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['username', 'batch']

class UserProfileView(generics.RetrieveUpdateDestroyAPIView):
   queryset=CustomUser.objects.all()
   serializer_class=UserProfileSerializer
   lookup_field = "username"
   
class UpdateUser(generics.UpdateAPIView):
     queryset=CustomUser.objects.all()
     serializer_class=UserProfileSerializer
     lookup_field = "username"



