from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.db import IntegrityError

def home(request):
    users = User.objects.all()
    return render(request, 'index.html', {'users': users})

def user_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
        
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if not username or not password:
            messages.error(request, 'Please provide both username and password')
            return render(request, 'login.html')
            
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next', 'dashboard')
            return redirect(next_url)
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

def user_register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
        
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if not all([username, email, password, confirm_password]):
            messages.error(request, 'Please fill in all fields')
            return render(request, 'register.html')
            
        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return render(request, 'register.html')
            
        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            messages.success(request, 'Registration successful! Please login.')
            return redirect('login')
        except IntegrityError:
            messages.error(request, 'Username already exists')
        except Exception as e:
            messages.error(request, 'An error occurred during registration')
    
    return render(request, 'register.html')

@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'You have been successfully logged out')
    return redirect('login')

@login_required
def user_ingridient(request):
    return render(request, 'ingridient.html')

@login_required
def user_menu(request):
    return render(request, 'menu.html')