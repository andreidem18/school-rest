from student.serializer import StudentSerializer
from rest_framework import serializers
from student.models import Student
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            permissions = (AllowAny, )
        elif self.request.method == 'DELETE':
            permissions = (IsAdminUser, )
        else: 
            permissions = (IsAuthenticated, )
        return [permission() for permission in permissions]
