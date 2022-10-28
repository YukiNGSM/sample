from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('forgot_password', views.Forgot_passwordView.as_view(), name='forgot_password'),
    path('', views.LoginView.as_view(), name='login'),
    path('password_reset', views.Password_resetView.as_view(), name='password_reset'),
    path('register', views.RegisterView.as_view(), name='register'),
]