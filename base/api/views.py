from django.shortcuts import render
from rest_framework import generics
from base.models import CustomUser
from .serializers import UserSerializer

# Create your views here.

class UserView(generics.ListAPIView):
    queryset= CustomUser.objects.all()
    serializer_class=UserSerializer