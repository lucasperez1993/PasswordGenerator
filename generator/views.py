from lib2to3.pgen2.pgen import generate_grammar
from django.shortcuts import render
import random
#from django.http import HttpResponse

def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    generated_password = ''

    length = int(request.GET.get('length'))
    upper = request.GET.get('uppercase')
    special = request.GET.get('special')
    nums = request.GET.get('numbers')

    if upper:
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if special:
        characters.extend(list('-+_!@#$%&/()*'))
    if nums:
        characters.extend(list('0123456789'))

    for x in range(length):
        generated_password += random.choice(characters)

    return render(request, 'generator/password.html', {'password': generated_password})
