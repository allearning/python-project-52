from django.urls import path

from task_manager.statuses.views import IndexStatusesView, StatusCreateView, StatusUpdateView, StatusDeleteView

# from .views import IndexUsersView, UserCreateView, UserUpdateView, UserDeleteView


urlpatterns = [
    path('', IndexStatusesView.as_view(), name='statuses'),
    path('create/', StatusCreateView.as_view(), name='create_status'),
    path('<int:pk>/update/', StatusUpdateView.as_view(), name='status_update'),
    path('<int:pk>/delete/', StatusDeleteView.as_view(), name='status_delete'),
]
