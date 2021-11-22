from django.db.models import fields
from rest_framework import serializers
from student.models import Student

from Trainer.models import Trainer

from calender.models import Calender

from course.models import Course
# from student.model import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=("first_name","last_name","age",)



class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Trainer
        fields=("first_name","last_name","age",)


class CalenderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Calender
        fields=("Event_venue",)



class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields=("Trainer",)