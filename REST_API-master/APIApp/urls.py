from django.urls import path
from APIApp import views

urlpatterns = [
    path('', views.getall),
    path('getid/<int:id>/', views.getid),
    path('savedata/', views.savedata),
    path('update/<int:id>', views.update),
    path('deleteid/<int:id>', views.deleteid),
]
