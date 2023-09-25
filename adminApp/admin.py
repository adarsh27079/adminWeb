from django.contrib import admin

# Register your models here.
from .models import studentsData

admin.site.register(studentsData)

from .models import Course
admin.site.register(Course)