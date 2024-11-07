from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_registros, name='listar_registros'),
    path('crear/', views.crear_registro, name='crear_registro'),
    path('editar/<int:id>/', views.editar_registro, name='editar_registro'),
    path('eliminar/<int:id>/', views.eliminar_registro, name='eliminar_registro'),
]
