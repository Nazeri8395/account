from rest_framework import serializers
from .models import CustomUser, Customer

class CustomerSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)  # فقط خواندنی
    email = serializers.EmailField(source='user.email', required=True)
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Customer
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password', 'phone_number', 'birth_date']
        
        
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = CustomUser(**user_data)
        user.set_password(validated_data.pop('password'))  # هش کردن پسورد
        user.save()
        customer = Customer.objects.create(user=user, **validated_data)
        return customer

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', {})
        if user_data:
            instance.user.email = user_data.get('email', instance.user.email)
            instance.user.first_name = user_data.get('first_name', instance.user.first_name)
            instance.user.last_name = user_data.get('last_name', instance.user.last_name)
            if 'password' in validated_data:
                instance.user.set_password(validated_data['password'])
            instance.user.save()
        
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.birth_date = validated_data.get('birth_date', instance.birth_date)
        instance.save()
        return instance
    
    
   
        
