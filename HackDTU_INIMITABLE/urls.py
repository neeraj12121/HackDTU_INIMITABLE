from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import main.views



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', main.views.home),
    url(r'^form/', main.views.form),
    url(r'^results/', main.views.results),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
