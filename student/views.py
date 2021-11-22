# from django import forms
# Create your views here.
# from _typeshed import FileDescriptor
from django import forms
from django.urls.conf import re_path
from student.models import Student
from django.shortcuts import redirect, render
from .forms import Studentregistrationform
from django.http.response import HttpResponse
from django.db.models.aggregates import StdDev
# from .forms import StudentRegistrationForm

def register_student(request):
     form=Studentregistrationform
     return render(request,"register_student.html",{"form":form})

def register_student(request):
     if request.method=="POST":
          form=Studentregistrationform(request.POST)
          if form.is_valid():
               form.saved()
     else:
         print("form.error")

     form=Studentregistrationform()
     return render(request,"register_student.html",{"form":form})


def student_list(request):
     students= Student.objects.all()
     return render(request,"student_list.html",{"students":students})



def  edit_student(request,id):
     student=Student.objects.get(id=id)
   
     if request.method=="POST":
          form=Studentregistrationform(request.POST,instance=student)
          if form.is_valid():
               form.save()

     else:
          form=Studentregistrationform(instance=student)
          return render(request,"edit_student.html",{"form":form})
     return redirect("register_student")


def student_profile(request,id):
          student=Student.objects.get(id=id)
          return render(request,"student_profile.html",{"student":student})

def delete_student(request,id):
          student=Student.objects.get(id=id)
          student.delete()
          return redirect("student_list")







