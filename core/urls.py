from django.urls import path
# from django.urls import urls
from.views import home

app_name="core"
urlpatterns=[
    path('',home, name="home"),
]


