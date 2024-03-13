from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from book_app.forms import BookStoreForm
from book_app.models import BookStoreModel
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy





# function based view
def home(req):
    return render(req, 'home.html')

# class based view---
class MyTemplateView(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {'name': 'TOPU', 'age': 21}
        print(context)
        context.update(kwargs) # contex updated
        print(context)
        return context





# def store_book(req):
#     if req.method == 'POST':
#         book = BookStoreForm(req.POST)
#         if book.is_valid():
#             book.save(commit=True)
#             print(book.cleaned_data)
#             return redirect('book_show')
#     else:
#         book = BookStoreForm()
#     return render(req, 'store_book.html', {'form':book})

# class BookFormView(FormView):
#     template_name = 'store_book.html'
#     form_class = BookStoreForm
#     success_url = reverse_lazy('book_show')
#     def form_valid(self, form):
#         print(form.cleaned_data)
#         form.save()
#         return redirect('book_show')

class BookFormView(CreateView):
    model = BookStoreModel
    template_name = 'store_book.html'
    form_class = BookStoreForm
    success_url = reverse_lazy('book_show')
    




# def show_book(req):
#     book = BookStoreModel.objects.all()
#     for item in book:
#         print("Date: ",item.last_pub)
#     return render(req, 'show_book.html', {'datas':book})

# class based view---
class BookStoreModelListView(ListView):
    model = BookStoreModel
    template_name='show_book.html'
    context_object_name = 'datas'
    # def get_queryset(self):
    #     return BookStoreModel.objects.filter()
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context = {'datas': BookStoreModel.objects.all().order_by('author')}
    #     return context
    # ordering = ['category']
    def get_template_names(self): # this function not implemented
        if self.request.user.is_superuser:
            template_name='show_book.html'
        elif self.request.user.is_staff:
            template_name='show_book.html'
        else:
            template_name=self.template_name
        return [template_name]
    
class BookStoreModelDetailView(DetailView):
    model = BookStoreModel
    template_name='book_details.html'
    context_object_name = 'data'
    pk_url_kwarg = 'id'





# def edit_book(req, id):
#     book = BookStoreModel.objects.get(pk=id)
#     form = BookStoreForm(instance=book)
#     if req.method == 'POST':
#         form = BookStoreForm(req.POST, instance=book)
#         if form.is_valid():
#             form.save(commit=True)
#             return redirect('book_show')
#     return render(req, 'store_book.html', {'form':form})

class BookUpdateView(UpdateView):
    model = BookStoreModel
    template_name = 'store_book.html'
    form_class = BookStoreForm
    success_url = reverse_lazy('book_show')





# def delete_book(req, id):
#     book = BookStoreModel.objects.get(pk=id).delete()
#     return redirect("book_show")

class DeleteBookView(DeleteView):
    model = BookStoreModel
    template_name = 'confermation.html'
    success_url = reverse_lazy('book_show')