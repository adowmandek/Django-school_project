from django.urls import path,include
from rest_framework import routers,urlpatterns
from .views import StudentViewSet

from .views import TrainerViewSet

from .views import CalenderViewSet

from .views import CourseViewSet


router=routers.DefaultRouter()
router.register("student/",StudentViewSet)
router.register("trainer/",TrainerViewSet)
router.register("calender/",CalenderViewSet)
router.register("course/",CourseViewSet)

urlpatterns=[
    path("",include(router.urls)),
]
