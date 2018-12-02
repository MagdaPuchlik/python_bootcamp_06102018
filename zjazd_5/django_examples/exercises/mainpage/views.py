from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,response

def main_page(request):
    return HttpResponse(content="Main Page")

def hello_world(request):
    return HttpResponse(content="Hello World")

def hello_personalized(request, name):
    return HttpResponse(content=f"Hello {name}")

def sum_no(request, no1,no2):
    wynik = int(no1)+int(no2)
    return HttpResponse(content=f"Wynik to {wynik}")

def sub_no(request, no1,no2):
    wynik = int(no1)-int(no2)
    return HttpResponse(content=f"Wynik to {wynik}")

def mul_no(request, no1,no2):
    wynik = int(no1)*int(no2)
    return HttpResponse(content=f"Wynik to {wynik}")

