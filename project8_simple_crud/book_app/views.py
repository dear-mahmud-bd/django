from django.shortcuts import render, redirect
from book_app.forms import BookStoreForm
from book_app.models import BookStoreModel
# Create your views here.
def home(req):
    return render(req, 'home.html')

def store_book(req):
    if req.method == 'POST':
        book = BookStoreForm(req.POST)
        if book.is_valid():
            book.save(commit=True)
            print(book.cleaned_data)
            return redirect('book_show')
    else:
        book = BookStoreForm()
    return render(req, 'store_book.html', {'form':book})

def show_book(req):
    book = BookStoreModel.objects.all()
    for item in book:
        print("Date: ",item.last_pub)
    return render(req, 'show_book.html', {'datas':book})

def edit_book(req, id):
    book = BookStoreModel.objects.get(pk=id)
    form = BookStoreForm(instance=book)
    if req.method == 'POST':
        form = BookStoreForm(req.POST, instance=book)
        if form.is_valid():
            form.save(commit=True)
            return redirect('book_show')
    return render(req, 'store_book.html', {'form':form})

def delete_book(req, id):
    book = BookStoreModel.objects.get(pk=id).delete()
    return redirect("book_show")