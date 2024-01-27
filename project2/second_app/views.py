from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def cources(request):
    return HttpResponse('''
                        <h1>This is Cources page...</h1>
                        <a href='/second_app/feedback/'> Feedback </a> <br>
                        <a href='/first_app/about/'> About </a> <br>
                        <a href='/first_app/contact/'> Contact </a> <br>
                        ''')

def feedback(request):
    return HttpResponse('''
                        <h1>This is Feedback page...</h1>
                        <a href='/second_app/cources/'> Cources </a> <br>
                        <a href='/first_app/about/'> About </a> <br>
                        <a href='/first_app/contact/'> Contact </a> <br>
                        ''')
