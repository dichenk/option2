from .models import CustomUser
from rest_framework import serializers

from django.contrib.auth.models import Group


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = CustomUser
 
    def create(self, validated_data):
        password = validated_data.get('password')
        user = CustomUser.objects.create(**validated_data)
        username = validated_data.get('username')
        user.set_password(password)
        user.save()
        return user
    
    def validate_password(self, attrs):
        if len(attrs) < 8:
            raise ValueError('Password must have at least 8 characters')
        if not any(letter.isdigit() for letter in attrs):
            raise ValueError('Password must include digits')
        return attrs
    
    def validate_email(self, attrs):
        if attrs.rfind('@mail.ru') == -1 and attrs.rfind('@yandex.ru') == -1:
            raise ValueError('domains allowed: mail.ru, yandex.ru')
        return attrs

    