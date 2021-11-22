# from schoolsystem.student.views import edit_student
from django.urls import path
from .views import course_list, course_profile, delete_course, edit_course, register_course
from django.shortcuts import render,redirect
urlpatterns=[
    path("register/",register_course,name="register_course"),
    path("list/",course_list,name="course_list"),
    path("edit/<int:id>/", edit_course, name="edit_student"),
    path("profile/<int:id>/", course_profile, name="course_profile"),
    path("delete/<int:id>/", delete_course, name="delete_course"),

    ]