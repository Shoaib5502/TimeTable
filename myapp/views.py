from django.shortcuts import render
from . import models

# Create your views here.


def admin_login(request):
    # Implement your login logic here
    return render(request, 'admin_login.html')


def admin_home(request):
    # Implement your admin home logic here
    return render(request, 'admin_home.html')
