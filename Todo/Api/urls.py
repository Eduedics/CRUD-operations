from django.urls import path
from . import views

urlpatterns = [
    path('tasks/view_all',views.taskListCreate.as_view()),
    # retriving single task
    path('tasks/<int:pk>/', views.taskRetrieveUpdateDestroy.as_view(), name='task-retrieve-update-destroy'),
    path('tasks/', views.taskListCreate.as_view(), name='task-list'),
    path('tasks/delete', views.taskListCreate.as_view(), name='task-list'),
]