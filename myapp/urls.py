from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('acceder', views.acceder, name='acceder'),
    path('registrar', views.registrar, name='registrar'),
    path('catalogo', views.catalogo, name='catalogo'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)