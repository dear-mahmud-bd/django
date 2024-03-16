from django import forms 
from first_app.models import ToDoListModel
from datetime import datetime

class ToDoListCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ToDoListCreateForm, self).__init__(*args, **kwargs)
        # Set initial value for start_date field to today's date
        self.fields['start_date'].widget.attrs['min'] = str(datetime.now().date())

    class Meta:
        model = ToDoListModel
        # exclude = ['id', 'status']
        fields = ['title', 'description', 'start_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 3}) 
        }
