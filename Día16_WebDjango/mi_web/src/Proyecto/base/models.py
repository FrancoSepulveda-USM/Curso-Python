from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tarea(models.Model):
    #Cada usuario puede tener múltiples tareas -> Relación 1:n
    #on_delete -> Que hacer cuando el usuario se elimina. blank -> El campo del registro puede estar en blanco.
    usuario = models.ForeignKey(User, on_delete=models.CASCADE,
                                null=True,blank=True) 
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(null=True,
                                blank = True)
    #Por defecto(default) es false.
    completada = models.BooleanField(default=False)
    #Genera automaticamente la fecha.
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    #Cuando se printee la clase, se imprime el titulo.
    def __str__(self):
        return self.titulo
    
    class Meta:
        #Como se ordenan las tareas en la tabla.
        #Los registros con completada=True quedan al final.
        ordering = ['completada']