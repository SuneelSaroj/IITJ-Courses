from django.contrib import admin

# Register your models here.

from .models import FirstSemesterCourse
from .models import SecondSemesterCourse


admin.site.register(FirstSemesterCourse)
admin.site.register(SecondSemesterCourse)
