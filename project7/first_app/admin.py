from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Student)
admin.site.register(models.TeacherInfoModel)

class StudentInfoModelAdmin(admin.ModelAdmin):
    list_display = ('roll', 'name', 'city')
admin.site.register(models.StudentInfoModel, StudentInfoModelAdmin)


@admin.register(models.EmployeeModel)
class EmployeeModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'city', 'designation')        
@admin.register(models.ManagerModel)
class ManagerModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'city', 'designation', 'take_interview', 'hiring')


@admin.register(models.Friend)
class FriendModelAdmin(admin.ModelAdmin):
    list_display = ('id','school', 'section', 'attendence', 'hw')
@admin.register(models.Me)
class MeModelAdmin(admin.ModelAdmin):
    list_display = ('id','school', 'section', 'attendence', 'hw')

@admin.register(models.Person)
class PersonModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'city', 'email')
@admin.register(models.Passport)
class PassportModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'pass_number', 'page', 'validity')

@admin.register(models.Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'post_cap', 'post_details', 'created_at')


@admin.register(models.Learner)
class LearnerModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'roll', 'class_name')
@admin.register(models.Teacher)
class TeacherModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'subject', 'student_list','mobile')