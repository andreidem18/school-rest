from classes.serializer import ClassSerializer
from classes.models import Class
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

class ClassViewSet(ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            permissions = (AllowAny, )
        elif self.request.method == 'DELETE':
            permissions = (IsAdminUser, )
        else: 
            permissions = (IsAuthenticated, )
        return [permission() for permission in permissions]