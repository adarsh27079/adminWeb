from django.db import models

# Create your models here.

class studentsData(models.Model):
   studentName = models.CharField(max_length=100)
   fathersName = models.CharField(max_length=100)
   mothersName = models.CharField(max_length=100)
   dob = models.DateField()
   gender = models.CharField(max_length=20)
   identity = models.CharField(max_length=20)
   indentityNum = models.IntegerField(default=0)
   email = models.EmailField(max_length=200)
   mobileNum = models.IntegerField()
   password = models.CharField(max_length=20)
   course=models.CharField(max_length=200, default='')
   image =models.ImageField(upload_to="profile/image", default='default/d.jpg')
   studentSign =models.ImageField(upload_to="signature/image", default='default/d.jpg')
   
   def __str__(self):
     return self.studentName


class Course(models.Model):
    course_name = models.CharField(max_length=100)
    studentsApplied = models.IntegerField(default=0)
    
    def __str__(self):
        return self.course_name


  
