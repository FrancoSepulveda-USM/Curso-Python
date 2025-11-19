import unittest
import cambia_texto

class ProbarCambiarTexto(unittest.TestCase):

    def test_mayus(self):
        palabra = 'buen dia'
        resultado = cambia_texto.mayuscula(palabra)
        self.assertEqual(resultado,'BUEN DIA')

if __name__ == '__main__':
    unittest.main()