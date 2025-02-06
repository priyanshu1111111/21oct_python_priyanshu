from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def contact(request):
    return render(request,'contact.html')
def t_detail(request):
    return render(request,'t_detail.html')
def t_list(request):
    return render(request,'t_list.html')
