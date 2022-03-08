import datetime
from dataclasses import field
from rest_framework import serializers
from .models import *

class UserServializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']


class ReviewSerializer(serializers.ModelSerializer):
    author = UserServializer(many=False, read_only=True)
    date_created = serializers.DateTimeField(default=datetime.date.today())
    class Meta:
        model = Review
        fields = "__all__"

    def create(self, validated_data):
        author = User.objects.get(pk=self.context.get('author', None))
        review = Review.objects.create(author=author, **validated_data)

        return review