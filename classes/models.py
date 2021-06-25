from django.db import models
from student.models import Student
from core.models import BaseModel

class Class(BaseModel):
    name = models.CharField(max_length=150)
    students = models.ManyToManyField(
        Student,
        related_name='classes'
    )

    def __str__(self):
        return self.name
