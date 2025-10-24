from rest_framework import serializers
from .models import Booking, Menu
from datetime import date

class BookingSerializer(serializers.ModelSerializer):
    def validate_booking_date(self, value):
        """Ensure booking date is not in the past"""
        if value < date.today():
            raise serializers.ValidationError("Booking date cannot be in the past.")
        return value
    
    def validate_no_of_guests(self, value):
        """Ensure number of guests is positive"""
        if value <= 0:
            raise serializers.ValidationError("Number of guests must be positive.")
        return value
    
    class Meta:
        model = Booking
        fields = ['id', 'name', 'no_of_guests', 'booking_date']

class MenuSerializer(serializers.ModelSerializer):
    def validate_price(self, value):
        """Ensure price is positive"""
        if value <= 0:
            raise serializers.ValidationError("Price must be positive.")
        return value
    
    def validate_inventory(self, value):
        """Ensure inventory is non-negative"""
        if value < 0:
            raise serializers.ValidationError("Inventory cannot be negative.")
        return value
    
    class Meta:
        model = Menu
        fields = ['id', 'title', 'price', 'inventory']
