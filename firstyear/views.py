from django.shortcuts import render

# Create your views here.
from .models import FirstSemesterCourse
from .models import SecondSemesterCourse


def courses(request):
    first_sem_course = FirstSemesterCourse.objects.all()
    second_sem_course = SecondSemesterCourse.objects.all()
    print(second_sem_course)

    return render(request, "./index.html", {'sem1': first_sem_course, 'sem2': second_sem_course})
