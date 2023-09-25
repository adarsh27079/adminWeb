from django.urls import path,include
from .import views

urlpatterns = [
   path('', views.index, name='index'),
   path('home', views.index, name='home'),
   path('about', views.about, name='about'),
   path('vm', views.vm , name='vm'),
   path('admission', views.admission, name='admission'), 
   #path('register', views.register, name='register'),
   path('login', views.auth, name='login'),
   path('register', views.register, name='register'),
   path('myAccount', views.myAccount, name='myAccount'),
   path('logout', views.logoutView, name='logout'),
]
