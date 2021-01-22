from rest_framework import generics
from rest_framework.viewsets import ModelViewSet

from .api.serializers import OrderSerializer, ServiceSerializer, ImageschemeSerializer
from .models import *

# ******************************УСЛУГИ************************************

class AdminServiceViewSet(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

# Вывод списка всех услуг
class ServiceListView(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


# Создание услуги
class ServiceCreateView(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


# Обновление конкретной услуги
class ServiceUpdateView(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


# Просмотр конкретной услуги
class ServiceRetrieveView(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


# Удаление конкретной услуги
class ServiceDestroyView(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

# ******************************ИЗОБРАЖЕНИЯ ПЛАН-СХЕМ************************************
# Вывод списка всех изображений план-схем
class ImageschemeListView(ModelViewSet):
    queryset = Imagescheme.objects.all()
    serializer_class = ImageschemeSerializer


# Создание изображения план-схемы
class ImageschemeCreateView(ModelViewSet):
    queryset = Imagescheme.objects.all()
    serializer_class = ImageschemeSerializer


# Обновление конкретного изображения план-схемы
class ImageschemeUpdateView(ModelViewSet):
    queryset = Imagescheme.objects.all()
    serializer_class = ImageschemeSerializer


# Просмотр конкретного изображения план-схемы
class ImageschemeRetrieveView(ModelViewSet):
    queryset = Imagescheme.objects.all()
    serializer_class = ImageschemeSerializer


# Удаление конкретного изображения план-схемы
class ImageschemeDestroyView(ModelViewSet):
    queryset = Imagescheme.objects.all()
    serializer_class = ImageschemeSerializer

# ******************************ЗАКАЗЫ************************************
# Вывод списка всех заказов
class OrderListView(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


# Создание заказа
class OrderCreateView(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


# Обновление конкретного заказа
class OrderUpdateView(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


# Просмотр конкретного заказа
class OrderRetrieveView(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


# Удаление конкретного заказа
class OrderDestroyView(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
