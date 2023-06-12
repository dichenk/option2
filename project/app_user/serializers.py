from .models import CustomUser
from rest_framework import serializers

from django.contrib.auth.models import Group


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ['username', 'password', 'phone_number', 'date_of_birth']
        model = CustomUser
 
    def create(self, validated_data):
        password = validated_data.get('password')
        user = CustomUser.objects.create(**validated_data)
        username = validated_data.get('username')
        user.set_password(password)
        user.save()
        return user