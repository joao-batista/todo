from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='task_list'),
    path('task_new/', views.task_new, name='task_new'),
    path('task_new_ajax/', views.task_new_ajax, name='task_new_ajax'),
    path('task_update/<int:id>', views.task_update, name='task_update'),
    path('task_delete/<int:id>', views.task_delete, name='task_delete'),
    path('task_delete_ajax/', views.task_delete_ajax, name='task_delete_ajax'),
    path('task_done/<int:id>', views.task_done, name='task_done'),
    path('task_undo/<int:id>', views.task_undo, name='task_undo'),
    path('task_done_ajax/', views.task_done_ajax, name='task_done_ajax'),
    path('task_undo_ajax/', views.task_undo_ajax, name='task_undo_ajax'),
    path('task_search/', views.task_search, name='task_search'),
]