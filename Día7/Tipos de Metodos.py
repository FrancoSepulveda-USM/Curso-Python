class Pajaro:

    #atributos de clase
    alas = True

    #Constructor para tener atributos de instancia
    def __init__(self,color,especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print("Pio Pio, mi color es {}".format(self.color))#Importante usar self para saber que se refiere al atributo de la instancia piolin

    def volar(self,metros):
        print(f"El pajaro ha volado {metros} metros")
        self.piar()#Al ser metodo normal(de instancia), puede llamar a otros metodos de la instancia

    def pintar_negro(self):
        self.color = "negro"

    @classmethod#Al ser metodo de clase no puede acceder a los atributos color ni especie, pues esos son atributos de instancia
    def poner_huevos(cls,cantidad):
        print("Puso {} huevos".format(cantidad))
        #print(f"Es de color {self.color}") <- Eso da error
        print(f"Tienes alas? {cls.alas}") #Si puede pues alas es atributo de clase

    @staticmethod
    def mirar(): #No puede modificar ni la instancia ni la clase
        #self.color = "rojo" <- Da error
        #cls.alas = False <- Da error
        #self.piar() <- Da error
        print("El pajaro mira")



#Met de instancia
piolin = Pajaro("amarillo","canario")
piolin.volar(50)
piolin.pintar_negro()
piolin.alas = False#Acceso directo al atributo de la clase
print(piolin.alas)


#Met de clase
Pajaro.poner_huevos(3)#Se puede usar directo al serr un metodo de clase
#Pajaro.piar() <- Da error pues piar es un metodo de instancia
piolin.poner_huevos(4)

#Met estatico
piolin.mirar()
Pajaro.mirar()