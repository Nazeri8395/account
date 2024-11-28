from djoser.serializers import UserCreateSerializer as DjoserUserCreateSerializer
from djoser.serializers import UserSerializer
from rest_framework import serializers
from accounts.models import Customer 

class UserCreateSerializer(DjoserUserCreateSerializer):
    
    class Meta(DjoserUserCreateSerializer .Meta):
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name']

class UserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
        
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'user', 'birth_date',]
        read_only_fields = ['user',  ]

