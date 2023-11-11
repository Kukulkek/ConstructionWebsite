from django.urls import path
from . import views
from .views import exit

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('logout/', exit, name='exit'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('servicios', views.servicios, name='servicios'),
    path('presupuesto', views.presupuesto, name='presupuesto'),
    path('add_to_budget/<int:material_id>/', views.add_to_budget, name='add_to_budget'),
    path('factura', views.factura, name='factura'),
    path('remove_from_budget/<int:material_id>/', views.remove_from_budget, name='remove_from_budget'),
    path('materiales', views.materiales, name='materiales'),
    path('materiales/crear', views.crear, name='crear'),
    path('materiales/editar', views.editar, name='editar'),
    path('materiales/editar/<int:id>', views.editar, name='editar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)