from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home_page'),
    
    path('show-task/', views.show_task, name='showtask_page'),
    
    path('add-task/', views.add_task, name='addtask_page'),
    path('edit-task/<int:pk>', views.edit_task, name='edittask_page'),
    path('delete-task/<int:pk>', views.delete_task, name='deletetask_page'),
    
    path('completed-task/', views.completed_task, name='completedtask_page'),
    path('complete-task/<int:pk>', views.complete_task, name='completetask_page'),
]