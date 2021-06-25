from rest_framework.serializers import ModelSerializer
from classes.models import Class

class ClassSerializer(ModelSerializer):
    class Meta:
        model = Class
        fields = ('id', 'name', 'students', 'created_at', 'updated_at')