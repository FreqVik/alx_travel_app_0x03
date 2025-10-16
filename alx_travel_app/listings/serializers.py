from .models import Listing, Booking
from rest_framework import serializers


class ListingSerializer(serializers.ModelSerializer):
    """Serializer for the Listing model"""
    
    class Meta:
        model = Listing
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    """Serializer for the Booking model"""
    
    class Meta:
        model = Booking
        fields = '__all__'