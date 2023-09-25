from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import studentsData
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.hashers import make_password
import requests
import json

# Create your views here.
def index(request):
   return render(request, 'index.html')
   
def about(request):
   return render(request, 'about.html')
   
def vm(request):
   return render(request, 'vm.html')
   
def admission(request):
   return render(request, 'admission.html')
   
   
#def register(request):
    #return render(request, 'register.html')
    
def auth(request):
   if request.method =='POST':
     username = request.POST['loginEmail']
     password = request.POST['loginPass']
     userAuth =authenticate(request, username=username, password=password)
     if userAuth is not None:
       login(request, userAuth)
       print(username, password)
       return redirect('home')
     else:
       return HttpResponse("username or password is incorrect")
     
   return render(request, 'login.html')
    
def register(request):
   if request.method =='POST':
      #funtion for student data
      studentName = request.POST['studentName']
      fathersName = request.POST['fathersName']
      mothersName = request.POST['mothersName']
      dob = request.POST['dob']
      gender = request.POST['gender']
      identity = request.POST['identity']
      idNum = request.POST['idNum']
      email = request.POST['email']
      confEmail = request.POST['confEmail']
      mobileNum = request.POST['mobileNum']
      confMobile = request.POST['confMobile']
      course = request.POST['selectedCourse']
      password = request.POST['password']
      confPassword = request.POST['confPass']
      studentImg = request.FILES.get('studentImg', None)
      studentSign = request.FILES.get('studentSign', None)
      
      if email!=confEmail:
        return HttpResponse('Confirm email is not matching')
      elif mobileNum!=confMobile or len(mobileNum) !=10:
        return HttpResponse('Confirm mobile number is not matching')
      elif password!=confPassword:
        return HttpResponse('Confirm password is not matching')
      else:
       # print(studentName, fathersName, mothersName,dob, gender, identity, idNum, email, mobileNum, password)
      #recptcha stuff
        hashed_password = make_password(password, hasher='default')
        clientKey = request.POST['g-recaptcha-response']
        secretKey = '6Le-2J4mAAAAAN46PaQPl377VIYv3jIksXaC2I_j'
        captchaData = {
          'secret': secretKey,
          'response': clientKey
        }
        response = requests.post('https://www.google.com/recaptcha/api/siteverify', data=captchaData)
        verify = response.json()['success']
        if verify:
          data = studentsData(studentName=studentName, fathersName=fathersName, mothersName=mothersName, dob=dob, gender=gender, identity=identity, indentityNum=idNum, email=email, mobileNum=mobileNum, password=hashed_password, course=course, image=studentImg, studentSign=studentSign )
          data.save()
          userData=User(username= confEmail, email=confEmail, password =hashed_password)
          userData.save()
          return redirect('login')
        else:
          return redirect('register')
          
   return render(request, 'register.html');
   
   
def myAccount(request):
    if request.user.is_authenticated:
        try:
            student = studentsData.objects.get(email=request.user.email)
            context = {
                'studentName': student.studentName,
                'fathersName': student.fathersName,
                'mothersName': student.mothersName,
                'dob': student.dob,
                'gender': student.gender,
                'identity': student.identity,
                'identityNum': student.indentityNum,
                'mobileNum': student.mobileNum,
                'email': student.email,
                'profile_pic_url' :student.image.url,
                'sign_pic_url':student.studentSign.url,
                'course':student.course,
            }
            return render(request, 'my-account.html', context)
        except studentsData.DoesNotExist:
            messages.error(request, 'Student data does not exist')
            return render(request, 'my-account.html')
    else:
        return redirect('login')

def logoutView(request):
   logout(request)
   return redirect('home')
   
   
