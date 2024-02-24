from django import forms 
from book_app.models import BookStoreModel

class BookStoreForm(forms.ModelForm):
    class Meta:
        model = BookStoreModel
        exclude = ['id']
        fields = ['book_name','author','category']
