from rest_framework import generics

from .api.serializers import UserSerializer
from .models import *


# Вывод списка всех юзеров
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Создание юзера
class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Обновление юзера
class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Просмотр конкретного юзера
class UserRetrieveView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Удаление конкретного юзера
class UserDestroyView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
