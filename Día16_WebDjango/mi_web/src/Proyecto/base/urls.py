from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy

# path(ruta_relativa, view, view_name)
urlpatterns = [
    path('', ListaPendientes.as_view(), name='tareas'),
    #int:pk es para poner el nro de la tarea(id en la bd) asociada a la url.
    path('login/',Logueo.as_view(), name='login'),
    #Cuando se desloguea lo manda a la pagina de login.
    path('logout/',LogoutView.as_view(next_page=reverse_lazy('login')), name='logout'),
    path('detalle-tarea/<int:pk>',DetalleTarea.as_view(), name='detalle'),
    path('crear-tarea/', CrearTarea.as_view(), name = 'crear-tarea'),
    path('editar-tarea/<int:pk>',EditarTarea.as_view(), name='editar-tarea'),
    path('eliminar-tarea/<int:pk>',EliminarTarea.as_view(), name='eliminar-tarea'),
    path('registro/',PaginaRegistro.as_view(),name='registro')
    ]