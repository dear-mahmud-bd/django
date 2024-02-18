from django.shortcuts import render, redirect
from . import models
from first_app.forms import StudentForms

# Create your views here.

def home(req):
    if req.method == 'POST':
        form = StudentForms(req.POST)    
        if form.is_valid() :
            form.save(commit=True) # save database or not
            # print(form.cleaned_data)
            return redirect('home')
    else:
        form = StudentForms()    
        
    # std = StudentForms()
    student = models.Student.objects.all()
    return render(req, "home.html", context={'data':student, 'form':form})

def delete_student(req, roll):
    std = models.Student.objects.get(pk=roll).delete()
    print (std)
    return redirect("homepage")