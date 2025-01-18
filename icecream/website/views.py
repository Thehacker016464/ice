from django.shortcuts import render,redirect
from .models import user
from django.contrib.auth import authenticate, login
from django.contrib import messages
def home(request):
    users = user.objects.all()
    return render(request, 'index.html', {'users': users})




def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password) 
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

def user_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user.objects.create_user(username=username, email=email, password=password)
        return redirect('login')
    return render(request, 'register.html')

def user_ingridient(request):
    return render(request, 'ingridient.html')

def user_menu(request):
    return render(request, 'menu.html')