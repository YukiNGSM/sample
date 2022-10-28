from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('match.urls')),
    path('account/', include('account.urls')),
    path('operation/', include('operation.urls')),
]