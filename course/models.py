from django.db import models
from django.db.models.fields import GenericIPAddressField

# Create your models here.

class Course(models.Model):
    Trainer=models.CharField(max_length=12,default=34,null=True,blank=True)
    presentations=models.CharField(max_length=12,default=30,null=True,blank=True)
    duration=models.PositiveSmallIntegerField(max_length=10,default=21,null=True,blank=True)
    course_material=models.FileField()
    results=models.PositiveSmallIntegerField(max_length=10,default=22,null=True,blank=True)
    id_Number=models.CharField(max_length=12,default=38,null=True,blank=True)
    profession=models.CharField(max_length=10,default=32,null=True,blank=True)
    Unit_Name=models.CharField(max_length=10,default=31,null=True,blank=True)


