from django.db import models

# Create your models here.
class Calender(models.Model):
    Event_venue=models.CharField(max_length=10,null=True,blank=True)
    Event_duration=models.DateTimeField(max_length=12,null=True,blank=True)
    Event_goal=models.CharField(max_length=13,null=True,blank=True)
    Event_signed_by=models.CharField(max_length=12,null=True,blank=True)
    Event_date=models.DateTimeField(max_length=10,null=True,blank=True)
    Event_atendee=models.IntegerField(max_length=10,null=True,blank=True)
    Event_name=models.CharField(max_length=12,null=True,blank=True)
    def __str__(self):
        return self.Event_venue


