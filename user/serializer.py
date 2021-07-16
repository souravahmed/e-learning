
from user.models import User
from rest_framework import serializers

from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from datetime import timedelta


class UserSerializer(serializers.ModelSerializer):
    """
    this serializer used only for creation user
    """
    confirm_password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['email', 'password', 'confirm_password','role', 'first_name', 'last_name']
        extra_kwargs = {
            'password': {'write_only': True},
            'id': {'read_only': True}
        }
    
    def create(self, validated_data):
        password = validated_data.get('password')
        confirm_password = validated_data.get('confirm_password')
        if password != confirm_password:
            raise serializers.ValidationError({'password': 'password should match with confirm password'})
        
        new_user_data = {}
        for key, value in validated_data.items():
            if key != 'confirm_password':
                new_user_data[key] = value
                
        return User.objects.create_user(**new_user_data)
    
    
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attr):
        data = super().validate(attr)
        data['_id'] = self.user.id
        data['access_token_expire_in_seconds'] = timedelta(days=1)
        data['refresh_token_expire_in_seconds'] = timedelta(days=2)
        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer