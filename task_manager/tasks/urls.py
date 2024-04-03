from django.urls import path

from task_manager.tasks.views import IndexTasksView, TaskCreateView, TaskUpdateView, TaskDeleteView


urlpatterns = [
    path('', IndexTasksView.as_view(), name='tasks'),
    path('create/', TaskCreateView.as_view(), name='create_task'),
    path('<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='stask_delete'),
]
