from rest_framework import serializers
from users.models import *
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.hashers import check_password

class verifySerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ['key']


class RegisterUserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self, **kwargs):
        name = self.validated_data['username']
        user = User(
            username=name.lower(),
            email=self.validated_data['email'],
        )
        
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'status':status.HTTP_400_BAD_REQUEST,'data': 'Passwords do not match'})
        user.set_password(password)
        user.save()
        return user




class tokenSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=50)






class userSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length=100)



class SetNewPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(
        min_length=6, max_length=68, write_only=True)
    # token = serializers.CharField(
    #     min_length=1, write_only=True)
    # uidb64 = serializers.CharField(
    #     min_length=1, write_only=True)

    class Meta:
        fields = ['password']

    def validate(self,attrs):
        token = self.context['token']
        uidb64 = self.context['id']
        # print(token,uidb64)
        try:
            password = attrs.get('password')
            id = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=id)
            if not PasswordResetTokenGenerator().check_token(user, token):
                raise serializers.ValidationError({'error': 'The rest link is invalid'})
            
            user.set_password(password)
            user.save()

            return (user)
        except Exception as e:
            raise serializers.ValidationError({'error': 'The rest link is invalid'})
        return super().validate(attrs)