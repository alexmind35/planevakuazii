from rest_framework import viewsets

from orders.api.serializers import OrderSerializer, ServiceSerializer, ImageschemeSerializer
from orders.models import Order, Service, Imagescheme


# Заказы
# Создавать заказы могут юзер и admin
class UserOrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class AdminOrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


# Услуги
# Создавать услуги может только admin

class AdminServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


# Изображения план-схем
# Создавать изображения план-схем может только admin

class AdminImageschemeViewSet(viewsets.ModelViewSet):
    queryset = Imagescheme.objects.all()
    serializer_class = ImageschemeSerializer
