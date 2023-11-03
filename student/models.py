from django.db import models
from utils.models import BaseModel
from sponsor.models import Sponsor


class StatusStudent(models.Choices):
    bakalavir = 'BAKALAVIR'
    magister = 'MAGISTER'


class University(models.Model):
    title = models.CharField(max_length=220)

    def __str__(self):
        return self.title


class Student(BaseModel):
    full_name = models.CharField(max_length=220)
    status = models.CharField(
        max_length=20, choices=StatusStudent.choices, default=StatusStudent.bakalavir
    )
    university_name = models.ForeignKey(University, on_delete=models.CASCADE)
    required_amount = models.IntegerField(default=0)
    payed_amount = models.IntegerField(default=0)


class StudentSponsor(BaseModel):
    sponsor_user = models.ForeignKey(Sponsor, on_delete=models.CASCADE)
    student_user = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
