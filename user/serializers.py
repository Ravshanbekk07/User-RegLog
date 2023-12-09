from .models import CustomUser
from rest_framework import serializers


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=['username','email','password']
        extra_kwargs={ 'password':{'write_only':True}}

    def create(self,validated_data):
        user=CustomUser(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class CustomUserTokenSerializer(serializers.Serializer):
    username=serializers.CharField(max_length=100)