import random
from django.shortcuts import render
from django.core.mail import send_mail

from .models import User 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken,AccessToken
from rest_framework import permissions

from App_Account.serializer import (UserRegisterSerializer,
                                   UserProfileViewSerializer,
                                   UserProfileUpdateViewSerializer
                                   )




class UserRegisterView(APIView):
    def post(self,request):
        serializer=UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success","message":"User Registration Successfull"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# class UserLoginView(APIView):
#     def post(self, request):
#         email = request.data.get('email')  # Corrected to use get()
#         password = request.data.get('password')  # Corrected to use get()
        
#         user = authenticate(request, email=email, password=password) 
  
#         if user:
#             refresh = RefreshToken.for_user(user)  # Fixed spelling of `refresh`
#             return Response({
#                 'status': "success",
#                 'message': "User Login Successful",
#                 'token': str(refresh.access_token),
#             },
#                             status=status.HTTP_200_OK
#                             )
        
#         return Response({
#             'status': "unauthorized",  # Fixed typo from `uauthorizes`
#             'message': "Invalid Credentials",
#         }, status=status.HTTP_401_UNAUTHORIZED)

class SendOtpView(APIView):
    def post(self,request):
        email=request.data.get("email")
        if not email or not User.objects.filter(email=email).exists():
            return Response({"status":"faild","message":"Email is required"},
                            status=status.HTTP_400_BAD_REQUEST
                            )
        otp=str(random.randint(1000,9999))
        user=User.objects.get(email=email)
        user.otp=otp
        user.save()
        send_mail(
            subject="OTP for Password Reset",
            message=f"your Otp Is {otp}",
            from_email=" OTP <otp@selesbakey.com>",
             recipient_list=[email],
            )
            
        return Response({"status":"success","message":"OTP Send Successfull"},
                        status=status.HTTP_200_OK)
            
        
        
class VeryfyOtpView(APIView):
    def post(self,requset):
        email=requset.data.get("email")
        otp=requset.data.get("otp")
        
        if not email or not otp:
            return Response({"status":"faild","message":"Email and OTP are required"},
                            status=status.HTTP_400_BAD_REQUEST
                            )
        try:
            user=User.objects.get(email=email,otp=otp)
            user.otp=None
            user.save()
            token=str(RefreshToken.for_user(user).access_token)
            return Response({"status":"success","message":"OTP verification Successful","token":token})
        except User.DoesNotExist:
                return Response({
                    "status":"faild",
                    "message":"Invalid OTP"
                },status=status.HTTP_400_BAD_REQUEST)
                
class ResetPasswordView(APIView):
    permission_classes=(
        permissions.IsAuthenticated
    )
    def post(self,request):
        password=request.data.get("password")
        if not password:
            return Response({"status":"faild","message":"password is required"},status=status.HTTP_400_BAD_REQUEST)
        user=request.user 
        user.set_password(password)
        user.save()
        
        print(user)
        return Response({"status":"success","message":"password reset successfull"},status=status.HTTP_200_OK)
        
class UserProfileView(APIView):
    def get(self, request):
        try: 
            user = request.user
            user_data = UserProfileViewSerializer(user).data
            return Response({
                "status": "success",
                "message": "request successful",
                "data": user_data
            }, status=status.HTTP_200_OK)
        
        except Exception as e:
            if not request.user or not request.user.is_authenticated:
                return Response({
                    "status": "failed",
                    "message": "user must be authenticated",
                }, status=status.HTTP_401_UNAUTHORIZED)
            
            # Handle other exceptions
            return Response({
                "status": "error",
                "message": f"An error occurred: {str(e)}",
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
            
class UserProfileUpdateView(APIView):
    permission_classes=(permissions.IsAuthenticated,)
    
    def post(self,request):
            user=request.user 
            serializer=UserProfileUpdateViewSerializer(user,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "status":"success",
                    "message":"profile update successfull"
                },status=status.HTTP_200_OK)
            
            return Response({
                "status": "error",
                "message": serializer.errors,
            }, status=status.HTTP_400_BAD_REQUEST)
            