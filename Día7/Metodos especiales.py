mi_lista = [1,1,1,1,1]
print(len(mi_lista))

class Objeto:
    pass

mi_objeto = Objeto()
#print(len(mi_objeto)) da error pues objeto no funciona con len.
print(mi_objeto) #Con un string representa la instancia del objeto.

class CD:
    def __init__(self,autor,titulo,canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones
    def __str__(self):
        return f"Album: {self.titulo} de {self.autor}"#Esto redefine lo que saldrá al poner print(mi_cd)

    def __len__(self):
        return self.canciones

    def __del__(self):
        print("Se ha eliminado el CD")


mi_cd = CD("Pink Floyd","The Wall",24)
print(mi_cd)
#Es lo mismo que
print(str(mi_cd))

#len(mi_cd) <- Da error ya que el metodo len no esta definido para clases por parte de python, pero yo la puedo modificar para que funcione en clases.
print(len(mi_cd))

del mi_cd #Elimina la instancia de mi_cd, hay que confiar en que lo elimina ya que no muestra nada
print(mi_cd)#Dice que no hay una instancia llamada mi_cd

#Pero si al usar del mi_cd quisiera que notifique si fue exitosa la eliminacion, puede modificar la funcion, de hecho puedo hacer lo que sea con esa funcion, si quiero la cambio para que no elimina nada. pero no es el caso.
print(mi_cd)