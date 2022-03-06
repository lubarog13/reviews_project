from dataclasses import field
from rest_framework import serializers
from .models import *

class UserServializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']


class ReviewSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    author = UserServializer(many = False)
    class Meta:
        model = Review
        fields = "__all__"