from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('password_reset', views.Password_resetView.as_view(), name='account_reset_password'),
    path('login', views.LoginView.as_view(), name='login'),
    path('password_reset_from_key', views.Password_reset_from_keyView.as_view(), name='password_reset_from_key'),
    path('signup', views.SignupView.as_view(), name='account_signup'),
]