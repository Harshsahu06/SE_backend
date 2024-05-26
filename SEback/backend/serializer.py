from .models import hospital,User
from rest_framework import serializers
class hospitaldataserializer(serializers.ModelSerializer):
    class Meta:
        model=hospital
        fields="__all__"
class userDataSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields="__all__"        
        