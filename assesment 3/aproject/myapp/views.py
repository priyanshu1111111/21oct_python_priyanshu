from django.shortcuts import render

# Create your views here.
def welcome(request):
    return render(request,'welcome.html')
def index(request):
    return render(request,'index.html')
def student(request):
    return render(request,'student.html')
def teschers(request):
    return render(request,'teachers.html')
def signup(request):
    return render(request,'signup.html')
def login(request):
    return render(request,'login.html')
def profile(request):
    return render(request,'profile.html')
def d_student(request):
    return render(request,'d_student.html')
def d_teacher(request):
    return render(request,'d_teacher.html')
def department(request):
    return render(request,'department.html')
def events(request):
    return render(request,'events.html')
