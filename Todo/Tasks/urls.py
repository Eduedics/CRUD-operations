from django.urls import path
from . import views

urlpatterns = [
    path('',views.ListTasks,name = 'home'),
    path('createtask', views.createTasks,name = 'update_createTasks'),
    path('update/<str:pk>/', views.updateTasks,name = 'update_createTasks'),
    path('delete/<str:pk>/', views.DeleteTasks,name = 'DeleteTasks')
]