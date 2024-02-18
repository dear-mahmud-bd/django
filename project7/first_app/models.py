from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField(primary_key=True)
    address = models.TextField()
    father = models.TextField(max_length=50)
    # father = models.TextField(blank=True)
    
    def __str__(self):
        return f"Roll: {self.roll}, Name: {self.name}, Father: {self.father}"

