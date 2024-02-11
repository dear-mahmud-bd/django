from django.shortcuts import render
from . forms import contactForm, StudentData, PasswordValidationProject

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



def form(req):
    # print(req.POST)
    return render(req, './first/form.html')



def DjangoForm(req):
    if req.method == 'POST':
        form = contactForm(req.POST, req.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            with open("./first_app/upload/" + file.name, "wb+") as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
                    
            print(form.cleaned_data)
    else:
        form = contactForm()
        
    return render(req, './first/djangoform.html', {'form':form})



def StudentForm(req):
    if req.method == 'POST':
        form = StudentData(req.POST, req.FILES)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = StudentData()
    return render(req, './first/djangoform.html', {'form':form})



def PasswordValidation(req):
    if req.method == 'POST':
        form = PasswordValidationProject(req.POST, req.FILES)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = PasswordValidationProject()
    return render(req, './first/djangoform.html', {'form':form})