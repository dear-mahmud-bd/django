from django.shortcuts import render
from django.http import HttpResponse

def home(req):
    return HttpResponse("My First Django Project")

def about(req):
    return HttpResponse("About Django Project")
