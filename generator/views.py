from django.shortcuts import render
from django.http import HttpResponse
import random
from info.views import info

def home(request):
    return render(request, 'generator/home.html')


def password(request):

    char = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
         char.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
         char.extend(list('~!@#$%^&*()'))
    if request.GET.get('numbers'):
        char.extend(list('0123456789'))

    length = int(request.GET.get('length', 12))
    password = ""
    for x in range(length):
        password+= random.choice(char)

    return render(request, 'generator/password.html', {'password':password})
