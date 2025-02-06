from django.contrib import admin
from django.urls import path
from finalapp import views

urlpatterns = [
    path('',views.index),
    path('contact/',views.contact,name='contact'),
    path('t_detail',views.t_detail,name='t_detail'),
    path('t_list/',views.t_list,name='t_list'),
]

