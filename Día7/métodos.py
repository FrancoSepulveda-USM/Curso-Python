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

piolin = Pajaro("amarillo","canario")
piolin.piar()
piolin.volar(50)