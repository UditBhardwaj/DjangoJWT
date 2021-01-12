from rest_framework import serializers

from .models import Usermodel


class RegistrationSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        max_length=128,

        write_only=True
    )



    class Meta:
        model = Usermodel
        fields = ['email', 'username', 'password']

    def create(self, validated_data):

        return Usermodel.objects.create_user(**validated_data)

class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,

        write_only=True
    )


    class Meta:
        model = Usermodel
        fields = ['email','password']