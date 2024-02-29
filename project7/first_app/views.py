from django.shortcuts import render, redirect
from . import models
from first_app.forms import StudentForms
from first_app.models import Teacher, Learner

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

def showData(req):
    # students list for one teacher
    teacher = Teacher.objects.get(name = 'Shamim Usman')
    students =teacher.student.all()
    for stud in students:
        print(f"{stud.name}, {stud.roll}, {stud.class_name}")
    
    # teachers list for one student
    learner = Learner.objects.get(name = 'MD. MAHMUDUL HASAN')
    # teachers =learner.teacher_set.all()
    teachers =learner.teachers.all()
    for teacher in teachers:
        print(f"{teacher.name}, {teacher.subject}, {teacher.mobile}")
    
    return render(req, 'show_data.html')
