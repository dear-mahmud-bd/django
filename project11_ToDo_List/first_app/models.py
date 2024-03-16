from django.db import models

# Create your models here.
class ToDoListModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    finish_time = models.DateTimeField(null=True, blank=True)
    status = models.BooleanField(default=False)