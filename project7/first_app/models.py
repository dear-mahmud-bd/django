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

# 1. abstruct base class
class CommonInfoModel(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    class Meta:
        abstract = True
class StudentInfoModel(CommonInfoModel):
    roll = models.IntegerField()
    payment = models.IntegerField()
    section = models.CharField(max_length=50)
class TeacherInfoModel(CommonInfoModel):
    salary = models.IntegerField()
        
# 2. multitable inheritance
class EmployeeModel(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=40)
    designation = models.CharField(max_length=20)
class ManagerModel(EmployeeModel):
    take_interview = models.BooleanField()
    hiring = models.BooleanField()

# 3. proxy model
class Friend(models.Model): # my friend present in the class room
    school = models.CharField(max_length=40)
    section = models.CharField(max_length=10)
    attendence = models.BooleanField()
    hw = models.CharField(max_length=50)
class Me(Friend): # i'm not in the class
    class Meta:
        proxy = True
        ordering = ['id']


# 1. one to one relationship
class Person(models.Model):
    name = models.CharField(max_length = 30)
    city = models.CharField(max_length=50)
    email = models.EmailField(max_length=30)
    def __str__(self):
        return f"{self.id}-{self.name}"
class Passport(models.Model):
    user = models.OneToOneField(to=Person, on_delete = models.CASCADE)
    pass_number = models.IntegerField()
    page = models.IntegerField()
    validity = models.IntegerField()       
   
# 2. one to many relationship
class Post(models.Model):
    user = models.ForeignKey(Person, on_delete=models.SET_NULL, null = True)
    post_cap = models.CharField(max_length=30)
    post_details = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
   
# 3. many to many relationship
class Learner(models.Model):
    name = models.CharField(max_length=30)
    roll = models.IntegerField()
    class_name = models.CharField(max_length=10)
    def __str__(self):
        return f"{self.id}-{self.name}"

class Teacher(models.Model):
    student = models.ManyToManyField(Learner, related_name='teachers')
    name = models.CharField(max_length=30)
    batch_no = models.IntegerField()
    subject = models.CharField(max_length=20)
    mobile = models.CharField(max_length=11)
    def student_list(self):
        return ", ".join([str(i) for i in self.student.all()])   
   
   