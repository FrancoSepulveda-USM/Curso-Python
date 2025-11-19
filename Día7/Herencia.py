class Animal:
    def __init__(self,edad,color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("Este animal nació")

class Pajaro(Animal):
    pass

print(Pajaro.__base__)#Muestra de cual clase es hija
print(Animal.__subclasses__())#Muestra las clases hijas de Animal

piolin = Pajaro(2,"negro")#Lo hereda de la clase padre, claro que la clase hija puede tener su propio constructor
piolin.nacer()#Lo heredó de la clase Animal
print(piolin.color)