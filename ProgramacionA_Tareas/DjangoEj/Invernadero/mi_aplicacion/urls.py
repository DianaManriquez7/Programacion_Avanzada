from django.urls import path
from mi_aplicacion.views import guardarDatosInvernadero, listarDatosInvernadero, editarDatosInvernadero, eliminarDatosInvernadero

urlpatterns = [
    path('registrarDatos/', guardarDatosInvernadero, name="registrarDatos"),
    path('registrarDatos/listarDatos/', listarDatosInvernadero, name="listarDatos"),
    path('editarDatos/<int:id>/', editarDatosInvernadero, name='editarDatos'),
    path('eliminarDatos/<int:id>/', eliminarDatosInvernadero, name='eliminarDatos'),
]