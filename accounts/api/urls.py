from django.urls import path
from accounts.views import UserListView, UserCreateView, UserUpdateView, UserRetrieveView, UserDestroyView

urlpatterns = [
    path('users/all', UserListView.as_view()),
    path('users/create', UserCreateView.as_view()),
    path('users/update/<int:pk>', UserUpdateView.as_view()),
    path('users/detail/<int:pk>', UserRetrieveView.as_view()),
    path('users/delete/<int:pk>', UserDestroyView.as_view()),
]
