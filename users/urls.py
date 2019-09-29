from django.contrib import admin
from django.urls import path, include
from users.views import *

urlpatterns = [
    path('user/create/', UserCreateView.as_view()),
    path('all/', UserListView.as_view()),
    path('user/detail/<int:pk>', UserDetailView.as_view())
]