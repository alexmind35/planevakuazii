from rest_framework import viewsets

from orders.api.serializers import OrderSerializer, ServiceSerializer, ImageschemeSerializer
from orders.models import Order, Service, Imagescheme


# Заказы
# Создавать заказы могут юзер и admin
class UserOrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        if not self.request.user.is_staff or not self.request.user.is_superuser:
            return Order.objects.filter(user=self.request.user)
        return Order.objects.all()


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
