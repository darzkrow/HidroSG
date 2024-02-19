from django.urls import path
from . import views
from .views import favicon

urlpatterns = [
    path('', views.Dashboard, name='dashboard'),
    path('visitante/', views.Listado_Filtro_Buscar,name='lista_visitantes'),
    path('detalle_visitante/<str:dni>/', views.detalleVisitante, name='detalle_visitante'),
    path('eliminarVisitante/<str:dni>/', views.delete_restore_visitor, name='borrado_visitante'),
    path('registrarAcceso/<int:visitor_id>/', views.add_access, name='add_access'),
    path('editarVisitante/<str:dni>/', views.edit_visitor, name='edit_visitor'),
    path('registrarvisitante/', views.add_visitor, name='crear_visitante'),
    path('papeleravisitante/', views.papelera, name='Papelera_Reciclaje'),
    
    
    
    path('favicon.ico', favicon),
]
