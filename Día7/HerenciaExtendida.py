"""
Sobreescribir atributos
class Animal:
    def __init__(self,edad,color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("Este animal nació")

    def hablar(self):
        print("Este animal emite un sonido")

class Pajaro(Animal):#Hereda la edad y color de la clase padre(color y edad), al crear su propio constructor redefine los valores de edad y color para la clase Pajaro

    def __init__(self,edad,color,altura_vuelo):#Define atributos propios de la clase Pajaro y redefine los de la clase padre
        #self.edad = edad
        #self.color = color
        #Otra forma de redefinir los valores de los atributos pertenecientes a la clase padre es con super
        super.__init__(edad,color)#Esto reemplaza a self.edad = edad y self.color = color
        self.altura_vuelo = altura_vuelo

    def hablar(self):#Sobreescribe el metodo del padre
        print("Pio")

    def volar(self,metros):#Crea su propio metodo
        print(f"El pajaro vuela {metros} metros")

piolin = Pajaro(2,"negro")#Metodo heredado y no modificado
piolin.hablar()
piolin.volar(300)


--------------------------------------------------------------
Herencias multiples
"""


class Padre():
    def hablar(self):
        print("Hola")

class Madre():
    def reir(self):
        print("Ja ja")

    def hablar(self):
        print("Que tal")

class Hijo(Padre,Madre):#Al poner padre primero que madre, eso significa que primero hereda de padre, por lo que los metodos que tengan madre y padre en comun, tendran preferencia los de padre
    pass

class Nieto(Hijo):#Como nieto hereda de hijo e hijo hereda de padre y madre, entonces nieto hereda de padre, madre e hijo.
    pass

mi_nieto = Nieto()
mi_nieto.hablar()#Primero hereda de padre y luego de madre
mi_nieto.reir()
print(Nieto.__mro__)#Emite el orden de preferencias de la clase Nieto.
#En este caso primero va Nieto, luego Hijo, luego Padre, luego Madre y por ultimo Object.