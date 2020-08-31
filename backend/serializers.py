from rest_framework import serializers
from backend.models import *
from rest_framework import status

class Contactusserializer (serializers.Serializer):
     class Meta:

         modal=Contactus
         fields = '__all__'