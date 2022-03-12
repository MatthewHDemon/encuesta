from django.contrib import admin
from django.urls import include, path

from django.config import setting
from django.config.urls.static import static

urlpatterns = [
    path('', include('polls.urls')),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

