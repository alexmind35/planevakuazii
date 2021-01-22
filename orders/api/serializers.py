from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from accounts.api.serializers import UserSerializer
from orders.models import Service, Order, Imagescheme




class OrderSerializer(ModelSerializer):
    user = UserSerializer()
    status_order = serializers.CharField(source='get_status_order_display')

    class Meta:
        model = Order
        fields = '__all__'

class ServiceSerializer(ModelSerializer):
    order = OrderSerializer()
    class Meta:
        model = Service
        fields = '__all__'



class ImageschemeSerializer(ModelSerializer):
    order = OrderSerializer()

    class Meta:
        model = Imagescheme
        fields = '__all__'