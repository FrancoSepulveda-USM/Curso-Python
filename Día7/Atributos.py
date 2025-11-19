from Día7.Clases import mi_pajaro


class Pajaro:

    #atributos de clase
    alas = True

    #Constructor para tener atributos de instancia
    def __init__(self,color,especie):
        self.color = color
        self.especie = especie

mi_pajaro = Pajaro("Negro","Tucan")
print(mi_pajaro.color) #color es el atributo
print(f"Mi pajaro de color {mi_pajaro.color} es un {mi_pajaro.especie}")
print(Pajaro.alas)
print(mi_pajaro.alas)