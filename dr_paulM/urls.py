"""URL configuration for dr_paulM project."""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail import urls as wagtail_urls   # <-- add this

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cms/', include(wagtailadmin_urls)),   # Wagtail admin UI
    path('documents/', include(wagtaildocs_urls)),
    path('api/', include('portfolio.api_urls')),
    path('', include('portfolio.urls')),        # your non-Wagtail pages

    path('', include(wagtail_urls)),            # <-- add this LAST
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
