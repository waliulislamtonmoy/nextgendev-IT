# from django.contrib.auth import get_user_model
# User =get_user_model

from App_Account.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    class Meta:
        model=User 
        fields=['email','password',]
    
    def create(self,validated_data):
        user=User.objects.create_user(**validated_data)
        user.save()
        return user    
    
class UserProfileViewSerializer(serializers.ModelSerializer):
    class Meta:
        model=User 
        fields=[
            "id",
            "firstName",
            "lastName",
            "email",
            "mobile",
            "image",
            "created_at",
            "updated_at"
        ]
    
    
class UserProfileUpdateViewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=User 
        fields=[
            "firstName",
            "lastName",
            "email",
            "password",
            "image",
            "mobile",
        ]
        extra_kwargs={
            'email':{
                "read_only":True
            }
        }
    def create(self,validated_data):
        user=User.objects.create_user(**validated_data)
        user.save()
        return user 