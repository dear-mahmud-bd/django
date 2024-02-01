from django import template
from django.template.loader import get_template

register = template.Library()

def my_template(value, arg):
    if arg=='change':
        value = 'TOPU'
        return value
    if arg=='title':
        return value.title()
register.filter('change_name', my_template)
    
    
def show_subjects():
    subjects = [
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
    ]
    return {'subjects': subjects}
subjects_template = get_template('first/items.html')
register.inclusion_tag(subjects_template)(show_subjects)
    