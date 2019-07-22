from django.shortcuts import render
from rest_framework import viewsets
from .models import Group
from .serializer import GroupSerializer, UserSerializer
from django.contrib.auth.models import User # If used custom user model

class GroupView(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer