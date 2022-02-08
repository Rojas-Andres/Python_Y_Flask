from django.shortcuts import render

import string 
from django.contrib.auth.models import User 
from django.utils.crypto import get_random_string

# Create your views here.

# Script para generar usuarios aleatorios
def create_user_random(cantidad):
    for i in range(cantidad):
        username = f'usuario_{get_random_string(5,string.ascii_letters)}'
        email = f'{username}@miempresa.com'
        password = get_random_string(10)
        User.objects.create(username=username,email=email,password=password)
    return f'{cantidad} usuarios creados correctamente ..! '