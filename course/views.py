from django.shortcuts import render

# Create your views here.

# from django import forms
# Create your views here.
from django import forms
from django.urls.conf import re_path
from django.shortcuts import redirect, render
from django.http.response import HttpResponse
from course.models import Course
from django.shortcuts import render
from .forms import Courseregistrationform
from django.db.models.aggregates import StdDev

# from .forms import StudentRegistrationForm

def register_course(request):
     form=Courseregistrationform
     return render(request,"register_course.html",{"form":form})

def register_course(request):
     if request.method=="POST":
          form=Courseregistrationform(request.POST)
          if form.is_valid():
               form.saved()
     else:
         print("form.error")

     form=Courseregistrationform()
     return render(request,"register_course.html",{"form":form})



def course_list(request):
     courses= Course.objects.all()
     return render(request,"course_list.html",{"courses":courses})




def  edit_course(request,id):
         course=Course.objects.get(id=id)
         if request.method=="POST":
          form=Courseregistrationform(request.POST,instance=course)
          if form.is_valid():
               form.save()

          else:
               form=Courseregistrationform(instance=course)
               return render(request,"edit_course.html",{"form":form})


def course_profile(request,id):
          course=Course.objects.get(id=id)
          return render(request,"course_profile.html",{"course":course})

def delete_course(request,id):
          course=Course.objects.get(id=id)
          course.delete()
          return redirect("course_list")










    