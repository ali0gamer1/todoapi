from django.shortcuts import render
from rest_framework import generics,mixins, permissions,authentication
from todo.models import Task
from .serializers import *

# Create your views here.

class TaskCreateAPIview(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [authentication.SessionAuthentication]

    """def perform_create(self, serializer):
        serializer.save()
        print(serializer)
    
    def get(self, req, *args, **kwargs):
        return self.create(req,*args, **kwargs)"""
    

class TaskDeleteAPIview(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TodoSerializer
    lookup_field = "pk"
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [authentication.SessionAuthentication]

    def perform_destroy(self, serializer):
        super().perform_destroy(serializer)
    
    def get(self,req, *args, **kwargs):
        return self.destroy(req, *args, **kwargs) 

class TaskDetailAPIview(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [authentication.SessionAuthentication]


class TaskUpdateAPIview(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TodoSerializer
    lookup_field = 'pk'
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [authentication.SessionAuthentication]
    
    def perform_update(self, serializer):
        instance = serializer.save()
    
    def get(self,req, *args, **kwargs):
        return self.update(req, *args, **kwargs) 
    