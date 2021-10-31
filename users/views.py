from rest_framework import generics
from django.contrib.auth.models import User
from users.models import Profile
from users.serializers import UserSerializer,ProfileSerializer


class UserList(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer 

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer 

class ProfileList(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer 

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer 