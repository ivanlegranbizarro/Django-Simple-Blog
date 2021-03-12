from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('', include('apps.theblog.urls')),
    re_path('members/', include('django.contrib.auth.urls')),
    re_path('members', include('apps.members.urls')),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
