from django.contrib import admin
from book_app.models import BookStoreModel
# Register your models here.

@admin.register(BookStoreModel)
class BookStoreModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'book_name', 'author', 'category')

# or-> admin.site.register(BookStoreModel,BookStoreModelAdmin)