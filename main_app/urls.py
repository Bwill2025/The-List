from django.urls import path
from . import views



urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('edit/<int:pk>/', views.task_edit, name='task_edit'),
    path('delete/<int:pk>/', views.task_delete, name='task_delete'),
    path('complete/<int:pk>/', views.task_complete, name='task_complete'),
    path('tasks/create/', views.TaskCreateView.as_view(), name='task_create_view'),
    path('tasks/', views.task_list, name='task_list'),
    path('accounts/signup/', views.signup, name='signup'),
]