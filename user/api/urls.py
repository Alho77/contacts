from django.urls import path

from user.api import views

app_name = 'user'

urlpatterns = [
    path('', views.UserListView.as_view(), name='list'),
    path('register/', views.SignUpView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]
