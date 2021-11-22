from django.shortcuts import render
# from student.models import Student
# from course.models import Course
# from Trainer.models import Trainer
# from calender.models import Calender


# Create your views here.
def home(request):
    return render(request,"home.html")
    # students=Student.objects.count()
    # courses=Course.objects.count()
    # trainers=Trainer.objects.count()


    # data={"students":students,"courses":courses,"trainers":trainers,}



