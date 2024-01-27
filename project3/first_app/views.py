from django.shortcuts import render

# Create your views here.
def cources(req):
    return render(req, './first_app/index.html', context={'admin':'TOPU', 'age':22, 'subjects':[
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
    ], 'blog': "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Reiciendis at animi aliquid mollitia labore commodi dolores eaque rem, dicta officia! Odio ipsam perferendis eos laboriosam enim aut reiciendis iure cum."})