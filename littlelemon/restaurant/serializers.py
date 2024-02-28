from rest_framework import serializers
from .models import Booking, MenuItem
from django.contrib.auth.models import User


# Booking and Menu models are imported from restaurant.models
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = "__all__"


# Serializer class for User model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']