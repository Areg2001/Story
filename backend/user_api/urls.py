from django.urls import path
from .views import ChangePassword, ChangeUserDataView
from . import views

urlpatterns = [
	path('register', views.UserRegister.as_view(), name='register'),
	path('login', views.UserLogin.as_view(), name='login'),
	path('logout', views.UserLogout.as_view(), name='logout'),
	path('user/', views.UserView.as_view(), name='user'),
    path("user/change_password/<int:pk>", ChangePassword.as_view()),
    path("user/change_data/<int:pk>", ChangeUserDataView.as_view()),
]