from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.templatetags.static import static
from django.urls import include, path, re_path
from django.views.generic.base import RedirectView
from wagtail import urls as wagtail_urls
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls

from home.views import AgrumentByDateRedirectView

urlpatterns = [
    path("favicon.ico", RedirectView.as_view(url=static("favicons/favicon.ico"))),
    path("django-admin/", admin.site.urls),
    path("admin/", include(wagtailadmin_urls)),
    path("documents/", include(wagtaildocs_urls)),
    # this is a hack because we cant use the wagtail page view since it does not support periods in the url
    re_path(
        r"agrument/(?P<day>\d{1,2})\.(?P<month>\d{1,2})\.(?P<year>\d{4})/$",
        AgrumentByDateRedirectView.as_view(),
        name="agrument-by-date",
    ),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Translatable URLs
# These will be available under a language code prefix. For example /en/search/
urlpatterns += i18n_patterns(
    path("trgovina/", include("shop.urls")),
    path("api/", include("home.urls")),
    path("", include(wagtail_urls)),
    prefix_default_language=False,
)
