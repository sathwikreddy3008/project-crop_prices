# crop_prices_app/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Crop, Price

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('crop_prices:prices')
        else:
            messages.error(request, 'Invalid login credentials.')
    return render(request, 'login.html')

@login_required(login_url='crop_prices:login')
def logout_view(request):
    logout(request)
    return redirect('crop_prices:login')

@login_required(login_url='crop_prices:login')
def prices(request):
    crops = Crop.objects.all()
    prices = Price.objects.filter(date__lte='2024-01-10')[:10]
    return render(request, 'prices.html', {'crops': crops, 'prices': prices})

def home(request):
    return render(request, 'home.html')

