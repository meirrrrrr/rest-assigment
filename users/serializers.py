from rest_framework import serializers
from users.models import User
from django.contrib.auth import password_validation
from django.contrib.auth.hashers import make_password

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


    def validate_password(self, value):
        password_validation.validate_password(value, self.instance)
        value = make_password(value)
        return value


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email')