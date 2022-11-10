from django.urls import path

from . import views

app_name = 'match'
urlpatterns = [
    path('chat',views.ChatView.as_view(), name="chat"),
    path('chat_list',views.Chat_listView.as_view(), name="chat_list"),
    path('edit_profile', views.Edit_profileView.as_view(), name="edit_profile"),
    path('home', views.HomeView.as_view(), name="home"),
    path('iine_me', views.Iine_meView.as_view(), name="iine_me"),
    path('inquiry', views.InquiryView.as_view(), name="inquiry"),
    path('member', views.MemberView.as_view(), name="member"),
    path('member_bye', views.Member_byeView.as_view(), name="member_bye"),
    path('point_free', views.Point_freeView.as_view(), name="point_free"),
    path('point_member', views.Point_memberView.as_view(), name="point_member"),
    path('random_match', views.Random_matchView.as_view(), name="random_match"),
    path('report', views.ReportView.as_view(), name="report"),
    path('search', views.SearchView.as_view(), name="search"),
    path('stop_service', views.Stop_serviceView.as_view(), name="stop_service"),
    path('terms_of_service', views.Terms_of_serviceView.as_view(), name="terms_of_service"),
]