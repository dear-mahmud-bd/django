from django.db import models

# Create your models here.
class BookStoreModel(models.Model):
    CATEGORY = (
        ('Mystery','Mystery'),
        ('Thriller','Thriller'),
        ('ScienceFiction','ScienceFiction'),
        ('Horror','Horror'),
        ('Humor','Humor'),
    )
    id = models.IntegerField(primary_key=True)
    book_name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    category = models.CharField(max_length=30, choices=CATEGORY)
    first_pub = models.DateTimeField(auto_now_add=True) # first time
    last_pub = models.DateTimeField(auto_now=True) # updatable
    
    def __str__(self):
        return f"Book Name: {self.book_name}, Author: {self.author}"
    