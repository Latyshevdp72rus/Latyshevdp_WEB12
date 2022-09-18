from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import redirect_site

urlpatterns = [
    path('', redirect_site),
    path('admin/', admin.site.urls),
    path('news/', include('app.olimp.urls')),
    path('account/', include('app.user.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)