from django.contrib import admin
from django.urls import path,include
from . import views
from django.views.generic import RedirectView   # redirect on to the blog's app
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',include('consumer.urls')),
    path('manufacturer/',include('manufacturer.urls')),
    path('producer/',include('producer.urls')),
    path('retailer/',include('retailer.urls')),
    path('wholesaler/',include('wholesaler.urls')),
    path('accounts/', include("django.contrib.auth.urls")),
    path('admin/', admin.site.urls),
    path('ajax/validate_username', views.validate_username, name="validate_username"),
             ]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)