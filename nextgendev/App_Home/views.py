from django.shortcuts import render
from django.shortcuts import get_object_or_404
from App_Home.models import Home
from App_Home.serializer import HomeSerializer
# Create your views here.
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions


class HomeListView(APIView):
    permission_classes=(permissions.IsAuthenticated,)
    
    def get(self,request):
        try:
            homeobjects=Home.objects.all()
            serializer=HomeSerializer(homeobjects,many=True)
            return Response({
                "status":"success",
                "data":serializer.data
            },status=status.HTTP_200_OK)
        except:
            return Response({
                "status":"failed",
            },status=status.HTTP_401_UNAUTHORIZED)
            
class HomeCreateView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        try:
            if Home.objects.exists():
                return Response({
                    "status": "failed",
                    "message": "You can only have one Home entry in the database."
                }, status=status.HTTP_400_BAD_REQUEST)
            
           
            serializer = HomeSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "status": "success",
                    "data": serializer.data
                }, status=status.HTTP_201_CREATED)
            return Response({
                "status": "failed",
                "errors": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({
                "status": "failed",
                "error": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            
class HomeUpdateView(APIView):
    permission_classes=(permissions.IsAuthenticated,)
    def put(self,request,pk):
        try:
            home = get_object_or_404(Home, pk=pk)
            serializer = HomeSerializer(home, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({
                "status":"success",
                "data":serializer.data
            },status=status.HTTP_201_CREATED)
        except:
            return Response({
                "status":"failed",
                
            },status=status.HTTP_400_BAD_REQUEST)
            
class HomeDeleteView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def delete(self, request, pk):
        try:
            home = get_object_or_404(Home, pk=pk)
            home.delete()
            return Response({
                "status": "success",
                "message": "Home entry deleted successfully."
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                "status": "failed",
                "error": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
        
        