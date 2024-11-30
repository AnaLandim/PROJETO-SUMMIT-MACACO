from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import re_path as url

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('students.urls')),
    url(r'^', include('schools.urls')),
    url(r'^', include('entries.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)