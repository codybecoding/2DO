from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskView, name='task'),
    path('add/', views.add, name='add'),
    path('delete/<int:id>/', views.delete, name='delete'),
]
