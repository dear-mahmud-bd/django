from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(req):
    return render(req, './first/home.html', context={'admin':'TOPU', 'age':22, 'subjects':[
        {
            'id':1,
            'name':'Data Stracture',
            'teacher': 'Anisiur Rahman'
        },
        {
            'id':2,
            'name':'OOPs',
            'teacher':'Aditya Rajbongsi'
        },
        {
            'id':3,
            'name':'Algorithm',
            'teacher':'Shakila Safiq'
        },
    ]})    

def about(req):
    return render(req, './first/about.html', context={'author' : 'ami tOPU'})

def subjects(req):
    return render(req, './first/subjects.html')