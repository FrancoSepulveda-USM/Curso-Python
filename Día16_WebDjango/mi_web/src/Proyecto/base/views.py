from django.shortcuts import render #Para mostrar en pantalla.
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView) #Tipo de pagina que representa lista de objetos.
from .models import * 
from django.urls import reverse_lazy #Para asociar el name de la url a la url.
from django.contrib.auth.views import LoginView #Para inicio de sesion
#from django.http import HttpResponse
# Create your views here.

'''def lista_pendientes(pedido):
    return HttpResponse('Lista de pendientes')
'''
#Requiere modelo y un query
class ListaPendientes(ListView):
    model = Tarea
    template_name = 'base/tarea_list.html'
    context_object_name = 'tareas'  #Nombre de la variable que se usara en la plantilla.
    
class DetalleTarea(DetailView):
    model = Tarea
    template_name = 'base/tarea_detail.html'
    context_object_name = 'tarea'
    
#Esto crea el formulario con nombre 'form'<- Usado en el html
class CrearTarea(CreateView):
    model = Tarea
    template_name = 'base/tarea_form.html'
    fields = '__all__' # Toma todos los campos de la tabla Tarea en la BD
    
    # Si el usuario completa con exito el formulario lo redirijo a otra pagina.
    success_url = reverse_lazy('tareas') # Pendientes es el name asociado a mi pagina principal en la url ''

#De forma estandar UpdateView y CreateView mandan por defecto al mismo templete si no pongo template_name
class EditarTarea(UpdateView):
    model = Tarea
    template_name = 'base/tarea_form.html'
    fields = '__all__' # Toma todos los campos de la tabla Tarea en la BD
    
    # Si el usuario completa con exito el formulario lo redirijo a otra pagina.
    success_url = reverse_lazy('tareas') # Pendientes es el name asociado a mi pagina principal en la url ''
    
class EliminarTarea(DeleteView):
    model = Tarea
    context_object_name = 'tarea'
    success_url = reverse_lazy('tareas')
    template_name = 'base/tarea_delete.html'

class Logueo(LoginView):
    template_name = "base/login.html"
    field = '__all__' #Toma todos los campos de loginview
    redirect_authenticated_user = True #Redirecciona al usuario autenticado
    
    def get_success_url(self): #Método para redirigir al usuario autenticado
        return reverse_lazy('tareas')
    