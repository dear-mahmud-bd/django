from django import forms 
from first_app.models import Student

class StudentForms(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        labels = {
            'roll':'Student roll',
            'name':'Student Name',
            'address':'Student Address',
            'father':'Student Father',
        }
        widgets = {
            'roll': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter student roll'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter student name'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter student address'}),
            'father': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter student father'}),
        }
        help_texts = {
            'roll': 'Enter student roll number',
            'name': 'Enter student name',
            'address': 'Enter student address',
            'father': 'Enter student father name',
        }
        error_messages = {
            'roll': {
                'required': "This field is required.",
                'unique': "A student with this roll number already exists.",
                # Add more custom error messages for the roll field as needed
            },
            'name': {
                'required': "This field is required.",
                # Add more custom error messages for the name field as needed
            },
            'address': {
                'required': "This field is required.",           
            },
            'father': {
                'required': "This field is required.",
            }
        }