from .models import Post
from rest_framework import serializers
from datetime import date


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Post
    
    def validate_headline(self, attrs):
        request = self.context.get('request')
        if any(something in attrs for something in ['ерунда', 'глупость', 'чепуха', 'бункерный дед']):
            raise ValueError('There are illegal words in the title')
        if date.today().year - request.user.date_of_birth.year < 18:
            raise ValueError('You should have at least 18 years old')
        return attrs