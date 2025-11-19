from datetime import datetime,time,date

mi_hora = time(17,35,50,1500)#Crea una variable de tipo hora
print(type(mi_hora))
print(mi_hora)
print(mi_hora.hour)
print(mi_hora.minute)


mi_dia = date(2025,10,18)#mi_dia es un objeto de tipo datetime, este es como el constructor.
print(mi_dia.ctime())#muestra un formato con el dia.
print(mi_dia.day)
print(mi_dia.year)
print(mi_dia.today())#Muestra la fecha actual

mi_fecha = datetime(2025,5,17,10,5,12)
print(mi_fecha)
print(type(mi_fecha))

#Calcular tiempos
nacimiento = date(1995,3,5)
defuncion = date(2095,6,19)
diferencia = defuncion-nacimiento
print(diferencia)

despierta = datetime(2022,10,5,7,30)
duerme = datetime(2022,10,5,23,45)
vigilia = duerme - despierta
print(vigilia.seconds)