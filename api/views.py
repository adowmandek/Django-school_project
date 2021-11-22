
from django.shortcuts import render
from rest_framework import viewsets
from student.models import Student
from .serializers import StudentSerializer

from Trainer.models import Trainer
from .serializers import TrainerSerializer



from calender.models import Calender
from .serializers import CalenderSerializer



from course.models import Course
from .serializers import CourseSerializer



# Create your views here.

class StudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer


class TrainerViewSet(viewsets.ModelViewSet):
    queryset=Trainer.objects.all()
    serializer_class=TrainerSerializer



class CourseViewSet(viewsets.ModelViewSet):
    queryset=Course.objects.all()
    serializer_class=CourseSerializer


class CalenderViewSet(viewsets.ModelViewSet):
        queryset=Calender.objects.all()
        serializer_class=CalenderSerializer