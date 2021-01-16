from rest_framework import serializers
from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    """
        Customer Serializer for the Customer model
    """
    class Meta:
        model = Customer
        fields = '__all__'
