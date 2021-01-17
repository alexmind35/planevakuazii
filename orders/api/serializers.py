from rest_framework import serializers

from accounts.api.serializers import UserSerializer
from ..models import Service, Imagescheme, Order


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'



class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    service = ServiceSerializer()
    status_order = serializers.CharField(source='get_status_order_display')

    class Meta:
        model = Order
        fields = '__all__'


class ImageschemeSerializer(serializers.ModelSerializer):
    order = OrderSerializer()

    class Meta:
        model = Imagescheme
        fields = '__all__'