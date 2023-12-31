from django.urls import path
from .views import RegisterView, LoginView, UserListView, UserRetrieveUpdateDestroyView

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),

    path('users', UserListView.as_view()),
    path('users/<str:username>', UserRetrieveUpdateDestroyView.as_view()),
]
