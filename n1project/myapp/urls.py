from django.contrib import admin
from django.urls import path
from myapp import views
from .forms import *
from .models import *

urlpatterns = [
    path('snippets/', views.snippet_list, name='snippet_list'),
    path('snippets/<int:pk>/', views.snippet_detail, name='snippet_detail'),
    path('comments/',views.comment_list, name='comment_list'),
]
