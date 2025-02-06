from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    
    path('',views.welcome),
    path('index/',views.index),
    path('signup/',views.signup),
    path('login/',views.login),
    path('student/',views.student,name='student'),
    path('teachers/',views.teschers,name='teachers'),
    path('profile/',views.profile),
    path('d_student/',views.d_student),
    path('d_teacher',views.d_teacher), 
    path('department/',views.department),
    path('events/',views.events),
    
]
