import bs4
import requests
from time import time as tm

url_base = 'https://books.toscrape.com/catalogue/page-{}.html'

ratingAlto = []
flag = True
# Itero las páginas
antes = tm()
for pagina in range(1, 51):

    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    
    sopa = bs4.BeautifulSoup(resultado.text, 'lxml')
    if flag:
        flag = False
        print(resultado)
        print(sopa,type(sopa))
    
    # Selecciono los datos de los libro
    libros = sopa.select('.product_pod')

    # iterar libros
    for libro in libros:
        # chequear que tengan 4 o 5 estrellas
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')) != 0:
            # Titulo Libro
            titulo_libro = libro.select('a')[1]['title']
            
            ratingAlto.append(titulo_libro)

# ver libros 4 u 5 estrellas en consola
for t in ratingAlto:
    print(t)

print(tm()-antes)