from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length = 10)
    password = serializers.CharField(min_length=6, required=True)
    password2= serializers.CharField(min_length=6, required=True, write_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'password', 'password2']
        
    
    def validate(self, attrs):
        p1 = attrs.get('password')
        p2 = attrs.get('password2')
        
        if p1 != p2:
            raise serializers.ValidationError('Passwords are not similar')
        return attrs
    
    
    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user