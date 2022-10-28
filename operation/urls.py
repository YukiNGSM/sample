from django.urls import path

from . import  views

app_name = 'operation'
urlpatterns = [
    path('ban_account', views.Ban_accountView.as_view(), name='ban_account'),
    path('check_age', views.Check_ageView.as_view(), name='check_age'),
    path('check_inquiry', views.Check_inquiryView.as_view(), name='check_inquiry'),
]