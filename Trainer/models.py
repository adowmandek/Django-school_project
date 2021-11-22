from django.db import models
from django.db.models.fields import GenericIPAddressField

# Create your models here.
class Trainer(models.Model):
    first_name=models.CharField(max_length=10,default=23,null=True,blank=True)
    last_name=models.CharField(max_length=10,default=20,null=True,blank=True)
    gender=models.CharField(max_length=12,default=30,null=True,blank=True)
    id_Number=models.CharField(max_length=12,default=35,null=True,blank=True)
    profession=models.CharField(max_length=10,default=45,null=True,blank=True)
    # photo=models.ImageField(max_length=10,)
    trainer_cv=models.FileField()
    age=models.CharField(max_length=12,default=24,null=True,blank=True)
    email=models.EmailField(max_length=20,default=30,null=True,blank=True)
    phoneNumber=models.PositiveIntegerField(max_length=13,default=41,null=True,blank=True)
    Unit_Name=models.CharField(max_length=10,default=23,null=True,blank=True)
    Bank_account=models.CharField(max_length=14,default=29,null=True,blank=True)










