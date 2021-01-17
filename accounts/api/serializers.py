from rest_framework import serializers

from accounts.models import User


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField()

    def save(self, **kwargs):
        user = super(UserCreateSerializer, self).save()
        user.set_password(self.validated_data.get('password'))
        user.save()
        return user

    class Meta:
        model = User
        fields = ['name', 'phone', 'email', 'password', 'organization_name', 'organization_address', 'photo']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'phone', 'email', 'organization_name', 'organization_address', 'photo']