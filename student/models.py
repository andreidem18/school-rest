from django.db import models
from core.models import BaseModel

class Student(BaseModel):
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    dob = models.DateField()

    def __str__(self):
        return self.firstname