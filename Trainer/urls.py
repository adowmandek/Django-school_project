from django.urls import path
from .views import delete_trainer, register_Trainer, trainer_list, trainer_profile,edit_trainer
from django.shortcuts import render,redirect
urlpatterns=[
    path("register/",register_Trainer,name="register_Trainer"),
    path("list/",trainer_list,name="trainer_list"),
    path("edit/<int:id>/", edit_trainer, name="edit_trainer"),
    path("profile/<int:id>/", trainer_profile, name="trainer_profile"),
    path("delete/<int:id>/", delete_trainer, name="delete_trainer"),


    ]