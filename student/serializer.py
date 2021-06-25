from rest_framework.serializers import ModelSerializer
from student.models import Student

class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'firstname', 'lastname', 'dob', 'classes', 'created_at', 'updated_at')