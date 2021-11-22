from django.core.exceptions import FieldError
from django.db import models
from django.db.models.fields.files import FieldFile, FileField


# Create your models here.
class Student(models.Model):
    first_name=models.CharField(max_length=10,null=True,blank=True)
    last_name=models.CharField(max_length=10,null=True,blank=True)
    age=models.PositiveIntegerField(max_length=10,null=True,blank=True)
    date_of_birth=models.DateField(max_length=20,null=True,blank=True)
    student_id_passport=models.CharField(max_length=13,null=True,blank=True)
    # gender=models.CharField(max_length=20)
    email=models.EmailField(max_length=35,null=50,blank=True)
    # nationality=models.Choices()
    phoneNumber=models.PositiveIntegerField(max_length=13,null=True,blank=True)
    registration=models.PositiveSmallIntegerField(max_length=10,null=True)
    county=models.CharField(max_length=13,null=True,blank=True)
    guardian_name=models.CharField(max_length=12,null=True,blank=True)
    contact_number=models.PositiveIntegerField(max_length=13,null=True,blank=True)
    medical_report=FileField(max_length=15,default=40,null=34,blank=True)
    class_name=models.CharField(max_length=13,default=40,null=True,blank=True)
    room_number=models.CharField(max_length=12,default=50,null=True,blank=True)
    # device_number=models.ForeignKey()
    mentors_name=models.CharField(max_length=12,default=47,null=True,blank=True)
    # languages=models.Choices()
    Big_sister=models.CharField(max_length=12,default=50,null=True,blank=True)
    # profile=models.ImageField(upload_to)="image"


def __str__(self):
        return self.first_name
def full_name(self):
        return f"{self.first_name}{self.last_name}"

