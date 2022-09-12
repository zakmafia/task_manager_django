from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_order/', views.create_order, name='create_order'),
    path('create_task/', views.create_task, name='create_task'),
    path('view_order/', views.view_order, name='view_order'),
    path('view_task/<slug>/', views.view_task, name='view_task'),
    path('delete_order/<order_id>/', views.delete_order, name='delete_order'),
    path('delete_task/<task_id>/', views.delete_task, name='delete_task'),
    path('edit_order/<order_id>/', views.edit_order, name='edit_order'),
    path('edit_task/<task_id>/', views.edit_task, name='edit_task'),
    path('do_task/<task_id>/', views.do_task, name="do_task"),
    path('finished_tasks/', views.view_finished_tasks, name="finished_tasks"),
]