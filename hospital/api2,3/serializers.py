from rest_framework import serializers
from .models import Client

class formserializer(serializers.ModelSerializer):
    class Meta():
        model = Client
        fields = '__all__'

    def create(self, validated_data):
        return Client.objects.create(**validated_data)