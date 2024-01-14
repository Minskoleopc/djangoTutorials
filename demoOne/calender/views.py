from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def january(request):
    return HttpResponse("I will start going to yoga classes")

def february(request):
    return HttpResponse("I will start going to dance classes")

def march(request):
    return HttpResponse("I will start going to coding classes")