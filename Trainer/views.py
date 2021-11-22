from django.shortcuts import render

# Create your views here.


# from django import forms
# Create your views here.
from django import forms
from Trainer.models import Trainer
from django.shortcuts import render
from .forms import Trainerregistrationform
from django import forms
from django.urls.conf import re_path
from django.shortcuts import redirect, render
from django.http.response import HttpResponse
from django.db.models.aggregates import StdDev


def register_Trainer(request):
     form=Trainerregistrationform
     return render(request,"register_trainer.html",{"form":form})

def register_Trainer(request):
     if request.method=="POST":
          form=Trainerregistrationform(request.POST)
          if form.is_valid():
               form.saved()
     else:
         print("form.error")

     form=Trainerregistrationform()
     return render(request,"register_trainer.html",{"form":form})


def trainer_list(request):
     trainers= Trainer.objects.all()
     return render(request,"trainer_list.html",{"trainers":trainers})


def  edit_trainer(request,id):
     trainer=Trainer.objects.get(id=id)
   
     if request.method=="POST":
          form=Trainerregistrationform(request.POST,instance=trainer)
          if form.is_valid():
               form.save()

     else:
          form=Trainerregistrationform(instance=trainer)
          return render(request,"edit_trainer.html",{"form":form})


def trainer_profile(request,id):
          trainer=Trainer.objects.get(id=id)
          return render(request,"trainer_profile.html",{"trainer":trainer})

def delete_trainer(request,id):
          trainer=Trainer.objects.get(id=id)
          trainer.delete()
          return redirect("trainer_list")


    
