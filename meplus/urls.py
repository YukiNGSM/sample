from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('match/', include('match.urls')),
    path('', include('allauth.urls')),
    path('operation/', include('operation.urls')),
]