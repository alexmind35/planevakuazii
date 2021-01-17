from rest_framework import generics
from rest_framework.viewsets import ModelViewSet

from .api.serializers import OrderSerializer, ServiceSerializer, ImageschemeSerializer
from .models import *


class AdminServiceViewSet(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

# ******************************УСЛУГИ************************************
# Вывод списка всех услуг
class ServiceListView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


# Создание услуги
class ServiceCreateView(generics.CreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


# Обновление конкретной услуги
class ServiceUpdateView(generics.UpdateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


# Просмотр конкретной услуги
class ServiceRetrieveView(generics.RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


# Удаление конкретной услуги
class ServiceDestroyView(generics.DestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

# ******************************ИЗОБРАЖЕНИЯ ПЛАН-СХЕМ************************************
# Вывод списка всех изображений план-схем
class ImageschemeListView(generics.ListAPIView):
    queryset = Imagescheme.objects.all()
    serializer_class = ImageschemeSerializer


# Создание изображения план-схемы
class ImageschemeCreateView(generics.CreateAPIView):
    queryset = Imagescheme.objects.all()
    serializer_class = ImageschemeSerializer


# Обновление конкретного изображения план-схемы
class ImageschemeUpdateView(generics.UpdateAPIView):
    queryset = Imagescheme.objects.all()
    serializer_class = ImageschemeSerializer


# Просмотр конкретного изображения план-схемы
class ImageschemeRetrieveView(generics.RetrieveAPIView):
    queryset = Imagescheme.objects.all()
    serializer_class = ImageschemeSerializer


# Удаление конкретного изображения план-схемы
class ImageschemeDestroyView(generics.DestroyAPIView):
    queryset = Imagescheme.objects.all()
    serializer_class = ImageschemeSerializer

# ******************************ЗАКАЗЫ************************************
# Вывод списка всех заказов
class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


# Создание заказа
class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


# Обновление конкретного заказа
class OrderUpdateView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


# Просмотр конкретного заказа
class OrderRetrieveView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


# Удаление конкретного заказа
class OrderDestroyView(generics.DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
