from rest_framework import generics
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated


from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed

from users.serializers import *


# from django.http import JsonResponse

class AuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        data={}
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            data['status'] = status.HTTP_200_OK
            data['msg'] = "You are Successfully Loggedin"
            data['data'] = {}
            data['data']['token'] = token.key
            data['data']['user_id'] = user.pk
            data['data']['username'] = user.username
            data['data']['email'] = user.email

            return Response(data)
        else :
            return Response({"msg":'Unable To Login With Provided Credentials','status':status.HTTP_400_BAD_REQUEST})

class verifyChangeToken(APIView):
    
    def post(self, request):
        serializer = tokenSerializer(data=request.data)
        data = dict()
        data['status'] = status.HTTP_400_BAD_REQUEST
        if serializer.is_valid():
            token = serializer.data.get('token')
            tokenObject = Token.objects.get(key=token)
            userObj = tokenObject.user
            tokenObject.delete()
            tokenObject = Token.objects.create(user=userObj)
            # tokenObject.save()
            data['status'] = status.HTTP_201_CREATED
            data['data'] = {}
            data['data']['token'] = tokenObject.key
            data['data']['userpk'] = userObj.pk
            data['data']['username'] = userObj.username
        return Response(data)


class RegisterUserView(APIView):
    
    def post(self, request):
        serializer = RegisterUserSerializer(data=request.data)
        data = {}
        
        name = request.data['username']
        name = name.lower()
     
        if (User.objects.filter(username=name).count())>0:
           
            return Response({'status':status.HTTP_400_BAD_REQUEST,'msg': {'username': 'Username Already Exists'}})

        if (User.objects.filter(email=request.data['email']).count())>0:
            return Response({'status':status.HTTP_400_BAD_REQUEST,'msg': {'email': 'This Email Is Already Being Used'}})

        if serializer.is_valid():
            
            user = User.objects.create_user(
                username=name.lower(),
                password=request.data['password'],
                email=request.data['email'],
                first_name=request.data['first_name'],
                last_name=request.data['last_name']
                )
            
            
            
            user.save()
            token, created = Token.objects.get_or_create(user=user)
            data['token'] = token.key
            data['status'] = status.HTTP_201_CREATED
            data['data'] =serializer.data
            data['data']['user_id'] = user.pk
            data['msg'] = 'You are Successfully Registered'
            print(data)
        else:
            
            data['status'] = status.HTTP_400_BAD_REQUEST
            data['msg'] = serializer.errors
        return Response(data)



class SetNewPasswordAPIView(generics.GenericAPIView):
    serializer_class = SetNewPasswordSerializer
    def patch(self,request,uidb64,token):
        serializer = self.serializer_class(data=request.data,context={'id':uidb64,'token':token})
        serializer.is_valid(raise_exception=True)
        return Response({'success': True, 'message': 'Password reset success'}, status=status.HTTP_200_OK)



class Logout(APIView):
    def get(self, request, format=None):
        # simply delete the token to force a login
        #request.user.auth_token.delete()
        return Response({
            'status': status.HTTP_200_OK
            
        })
