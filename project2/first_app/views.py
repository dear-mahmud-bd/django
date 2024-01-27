from django.shortcuts import render
from django.http import HttpResponse

def contact(request):
    return HttpResponse('''
                        <h1>This is Contact page...</h1>
                        <a href='/first_app/about/'> About </a> <br>
                        <a href='/second_app/cources/'> Cources </a> <br>
                        <a href='/second_app/feedback/'> Feedback </a> <br>
                        ''')

def about(request):
    return HttpResponse('''
                        <h1>This is About page...</h1>
                        <a href='/first_app/contact/'> Contact </a> <br>
                        <a href='/second_app/cources/'> Cources </a> <br>
                        <a href='/second_app/feedback/'> Feedback </a> <br>
                        ''')
