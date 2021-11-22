from django.shortcuts import render

# Create your views here.


# from django import forms
# Create your views here.
from django import forms
from django.urls.conf import re_path
from calender.models import Calender
from django.shortcuts import redirect, render
from django.shortcuts import render
from django.http.response import HttpResponse
from django.db.models.aggregates import StdDev
from.forms import Calenderregistrationform



# from .forms import Calenderregistrationform

def register_calender(request):
     form=Calenderregistrationform
     return render(request,"register_calender.html",{"form":form})

def register_calender(request):
     if request.method=="POST":
          form=Calenderregistrationform(request.POST)
          if form.is_valid():
               form.save()
     else:
         print("form.error")

     form=Calenderregistrationform()
     return render(request,"register_calender.html",{"form":form})


def calender_list(request):
     calenders= Calender.objects.all()
     return render(request,"calender_list.html",{"calenders":calenders})


def  edit_calender(request,id):
     calender=Calender.objects.get(id=id)

     if request.method=="POST":
          form=Calenderregistrationform(request.POST,instance=calender)
          if form.is_valid():
               form.save()

     else:
          form=Calenderregistrationform(instance=calender)
          return render(request,"edit_calender.html",{"form":form})


def calender_profile(request,id):
          calender=Calender.objects.get(id=id)
          return render(request,"calender_profile.html",{"calender":calender})

def delete_calender(request,id):
          calender=Calender.objects.get(id=id)
          calender.delete()
          return redirect("calender_list")







