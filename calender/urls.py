
# from schoolsystem.course.views import calender_profile
from django.urls import path
from .views import calender_list, delete_calender, register_calender,edit_calender,calender_profile
from django.shortcuts import render,redirect

urlpatterns=[
    path("register/",register_calender,name="register_calender"),
    path("list/",calender_list,name="calender_list"),
    path("edit/<int:id>/", edit_calender, name="edit_calender"),
    path("profile/<int:id>/", calender_profile, name="calender_profile"),
    path("delete/<int:id>/", delete_calender, name="delete_calender"),
]