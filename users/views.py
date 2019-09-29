from django.shortcuts import render
from rest_framework import generics
from users.serializers import UserDetailSerializer, UserListSerializer
from users.models import User

class UserCreateView(generics.CreateAPIView):
    serializer_class = UserDetailSerializer


class UserListView(generics.ListAPIView):
    serializer_class = UserListSerializer
    queryset = User.objects.all()

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserDetailSerializer
    queryset = User.objects.all()
