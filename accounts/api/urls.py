from django.urls import path
from accounts.views import UserListView, UserCreateView, UserUpdateView, UserRetrieveView, UserDestroyView

urlpatterns = [
    path('all', UserListView.as_view()),
    path('create', UserCreateView.as_view()),
    path('update/<int:pk>', UserUpdateView.as_view()),
    path('detail/<int:pk>', UserRetrieveView.as_view()),
    path('delete/<int:pk>', UserDestroyView.as_view()),
]
