from rest_framework import serializers

from accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'phone', 'email', 'organization_name', 'organization_address', 'photo']