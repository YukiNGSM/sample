from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import static

from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('match.urls')),
    # path('', include('allauth.urls')),
    path('operation/', include('operation.urls')),
]

#開発サーバでメディアを配信できるように設定
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA＿ROOT)