from django.urls import path

from webapp.views.base import index_view
from webapp.views.tasks import  add_view, DetailView, UpdateView, delete_view, confirm_delete, TasksView

urlpatterns = [
    path('', index_view, name='index'),
    path('tasks', TasksView.as_view(), name='tasks_view'),
    path('task/<int:pk>/', DetailView.as_view(), name='detail_view'),
    path('tasks/add', add_view, name='add_view'),
    path('task/<int:pk>/update/', UpdateView.as_view(), name='task_update'),
    path('task/<int:pk>/delete/', delete_view, name='task_delete'),
    path('task/<int:pk>/confirm_delete/', confirm_delete, name='confirm_delete')
]
