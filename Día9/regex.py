import re
numero_celular = r'\+569\d{8}'
texto = "Mi numero es +56979466943"
print(re.findall(numero_celular,texto))

texto = "Si necesitas ayuda llama al (658)-580-9955 las 24 horas al servicio de ayuda online"

patron = "ayuda"

busqueda = re.search(patron,texto)
print(busqueda)

busqueda = re.findall(patron,texto)
print(busqueda)
print(len(busqueda))

busqueda = re.findall(patron,texto)
for hallazgo in re.finditer(patron,texto):
    print(hallazgo.span())


texto2="llama al 564-525-6588 ya mismo"
patron = r"\d\d\d-\d\d\d-\d\d\d\d"
resultado = re.search(patron,texto2)
print(resultado)
print(resultado.group())

patron = re.compile(r"(\d{3}-)(\d{3})-(\d{4})")
resultado = re.search(patron,texto2)
print(resultado.group(1))
print(resultado.group(2))
print(resultado.group(3))


clave = input("Clave: ")
patron = r'\D\w{7}'
chequear = re.search(patron,clave)
print(chequear)


texto = "no atendemos los lunes por la tarde"
buscar = re.search(r"lunes|martes",texto)
print(buscar)