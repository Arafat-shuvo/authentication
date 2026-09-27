from django.shortcuts import render, redirect
from django.contrib.auth.models import User    
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def register_page(request):
    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        student_email = request.POST.get('student_email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            
            User.objects.create_user(
                username=student_name,
                email=student_email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )
            return redirect('login_page')  
        else: 
            print("Password and Confirm Password do not match.")
    return render(request, 'register.html')

def login_page(request):
    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        password = request.POST.get('password')

        user = authenticate(request, username=student_name, password=password)
        if user:
            login(request, user)
            return redirect('home_page')  
        else:
            print("Invalid credentials.")
    return render(request, 'login.html')        
def home_page(request):
    return render(request, 'home.html')

def logout_view(request):
    logout(request)
    return redirect('login_page')   