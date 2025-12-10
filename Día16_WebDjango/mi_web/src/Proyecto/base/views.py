from django.shortcuts import render, redirect #Para mostrar en pantalla.
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView, FormView) #Tipo de pagina que representa lista de objetos.
from .models import * 
from django.urls import reverse_lazy #Para asociar el name de la url a la url.
from django.contrib.auth.views import LoginView #Para inicio de sesion
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
#from django.http import HttpResponse
# Create your views here.

'''def lista_pendientes(pedido):
    return HttpResponse('Lista de pendientes')
'''
#Requiere modelo y un query
class ListaPendientes(LoginRequiredMixin,ListView):
    model = Tarea
    template_name = 'base/tarea_list.html'
    context_object_name = 'tareas'  #Nombre de la variable que se usara en la plantilla.
    
    #Para mostrar solo las tareas del usuario que esta logeado.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tareas']=context['tareas'].filter(usuario = self.request.user)
        context['count']=context['tareas'].filter(completada = False).count()
        
        #Busco solo las tareas que el usuario busco en la barra de busqueda
        valor_buscado = self.request.GET.get('area-buscar') or ''
        if valor_buscado:
            context['tareas']=context['tareas'].filter(titulo__icontains = valor_buscado)
        
        #Para que en el template quede guardado en la barra de busqueda el valor buscado
        context['valor_buscado']=valor_buscado
        return context
        
    
class DetalleTarea(LoginRequiredMixin,DetailView):
    model = Tarea
    template_name = 'base/tarea_detail.html'
    context_object_name = 'tarea'
    
#Esto crea el formulario con nombre 'form'<- Usado en el html
class CrearTarea(LoginRequiredMixin,CreateView):
    model = Tarea
    template_name = 'base/tarea_form.html'
    fields = ['titulo','descripcion','completada'] # Toma todos los campos de la tabla Tarea en la BD
    
    # Si el usuario completa con exito el formulario lo redirijo a otra pagina.
    success_url = reverse_lazy('tareas') # Pendientes es el name asociado a mi pagina principal en la url ''

    #Para que automaticamente sepa el usuario
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super(CrearTarea,self).form_valid(form)
    
#De forma estandar UpdateView y CreateView mandan por defecto al mismo templete si no pongo template_name
class EditarTarea(LoginRequiredMixin,UpdateView):
    model = Tarea
    template_name = 'base/tarea_form.html'
    
    #Solo estos campos
    fields = ['titulo','descripcion','completada'] # Toma todos los campos de la tabla Tarea en la BD
    
    # Si el usuario completa con exito el formulario lo redirijo a otra pagina.
    success_url = reverse_lazy('tareas') # Pendientes es el name asociado a mi pagina principal en la url ''
    
class EliminarTarea(LoginRequiredMixin,DeleteView):
    model = Tarea
    context_object_name = 'tarea'
    success_url = reverse_lazy('tareas')
    template_name = 'base/tarea_delete.html'

class Logueo(LoginView):
    #Asocia la url del logueo al template login_usuario
    template_name = "base/login_usuario.html"
    field = '__all__' #Toma todos los campos de loginview
    redirect_authenticated_user = True #Redirecciona al usuario autenticado, success_url es donde lo redirige.
    
    def get_success_url(self): #Método para redirigir al usuario autenticado, a donde lo redirige.
        return reverse_lazy('tareas')
    
class PaginaRegistro(FormView):
    template_name = 'base/registro.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tareas')
    
    #Devuelve lo que hay en la instancia de PaginaRegistro con toda la info agregada en el form.
    def form_valid(self, form):
        usuario = form.save()
        if usuario is not None:
            login(self.request, usuario)
        return super(PaginaRegistro,self).form_valid(form)
    
    #Para que cuando un usuario este registrado, no pueda acceder nuevamente a la página de registro.
    def get(self,*args,**kwargs):
        #Si esta autenticado no puede acceder a registro/, lo devuelve a la lista de tareas
        if self.request.user.is_authenticated:
            return redirect('tareas')
        
        #Si no esta autenticado, entonces entra a esta view de forma normal.
        return super(PaginaRegistro,self).get(*args,**kwargs)