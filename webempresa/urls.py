"""webempresa URL Configuration"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [

    # Rutas del la app CORE
    path('', include('core.urls')),

    # Rutas de la app Services.
    path('services/', include('services.urls')),

    # Rutas de la app Post
    path('blog/', include('blog.urls')),

    # Rutas de la app Pages
    path('page/', include('pages.urls')),

    # RUta de la app contact
    path('contact/', include('contact.urls')),

    # Ruta de administración
    path('admin/', admin.site.urls)
]

# validamos si estamos en modo debug
if settings.DEBUG:
    # para usar archivos staticos(img)
    from django.conf.urls.static import static

    # agregar a los patrones de url, path de la imagen.
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
