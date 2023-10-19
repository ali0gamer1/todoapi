from django.shortcuts import render
from rest_framework import generics,mixins, permissions,authentication
from todo.models import Task
from .serializers import *
from rest_framework.permissions import BasePermission

# Create your views here.

class CanViewObjectPermission(permissions.DjangoModelPermissions):
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }

    def has_permission(self, request, view):
        
        if not request.user.is_staff:
            return False
        
        return super().has_permission(request, view)


#USER VIEWS:
class TaskUserCreateAPIview(generics.ListCreateAPIView):
    #queryset = Task.objects.all()
    serializer_class = TodoUserSerializer
    permission_classes = [CanViewObjectPermission,permissions.IsAuthenticated]
    authentication_classes = [authentication.SessionAuthentication]
    model = Task

    def get_queryset(self):
        return self.model.objects.filter(user = self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        print(serializer)
        

    
    """
    def get(self, req, *args, **kwargs):
        return self.create(req,*args, **kwargs)"""
    

class TaskUserDeleteAPIview(generics.DestroyAPIView):
    #queryset = Task.objects.all()
    serializer_class = TodoUserSerializer
    lookup_field = "pk"
    model = Task
    permission_classes = [CanViewObjectPermission,permissions.IsAuthenticated]
    authentication_classes = [authentication.SessionAuthentication]

    def get_queryset(self):
        return self.model.objects.filter(user = self.request.user)

    def perform_destroy(self, serializer):
        super().perform_destroy(serializer)
    
    def get(self,req, *args, **kwargs):
        return self.destroy(req, *args, **kwargs) 

class TaskUserDetailAPIview(generics.RetrieveAPIView):
    #queryset = Task.objects.all()
    serializer_class = TodoUserSerializer
    model = Task
    permission_classes = [CanViewObjectPermission,permissions.IsAuthenticated]
    authentication_classes = [authentication.SessionAuthentication]
    
    def get_queryset(self):
        return self.model.objects.filter(user = self.request.user)


class TaskUserUpdateAPIview(generics.UpdateAPIView):
    #queryset = Task.objects.all()
    serializer_class = TodoUserSerializer
    lookup_field = 'pk'
    permission_classes = [CanViewObjectPermission,permissions.IsAuthenticated]
    authentication_classes = [authentication.SessionAuthentication]
    model = Task
    def get_queryset(self):
        return self.model.objects.filter(user = self.request.user)


    def perform_update(self, serializer):
        instance = serializer.save()
    
    def get(self,req, *args, **kwargs):
        return self.update(req, *args, **kwargs) 





#ADMIN VIEWS:
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
    