from django.urls import path

from .views import IndexUsersView, UserCreateView, UserUpdateView #, UserDeleteView


urlpatterns = [
    path('', IndexUsersView.as_view(), name='users'),
    path('create/', UserCreateView.as_view(), name='sign_in'),
    path('<int:pk>/update/', UserUpdateView.as_view(), name='user_update'),
#    path('<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),
]
