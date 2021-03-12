from rest_framework import serializers
from .models import User

class UserRegisterSerializer1(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(email=validated_data['email'], password=validated_data['password'],
                                        last_name=validated_data['last_name'], first_name=validated_data['first_name'])

        return user
