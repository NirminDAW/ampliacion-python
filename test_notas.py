import unittest
from notas import calcularNotaMaxima, calcularNotaMinima, calcularNotaMedia

class MyTestCase(unittest.TestCase):
    def testMaximoSencillo(self):
        self.assertEqual(calcularNotaMaxima(5.0, 7.0, 9.0), 9.0)

    def testMaximoDoble(self):
        self.assertEqual(calcularNotaMaxima(8.0, 9.0, 9.0), 9.0)

    def testMinimoVariandoOrden(self):
        self.assertEqual(calcularNotaMinima(3.0, 7.0, 9.0), 3.0)
        self.assertEqual(calcularNotaMinima(7.0, 9.0, 3.0), 3.0)
        self.assertEqual(calcularNotaMinima(7.0, 3.0, 9.0), 3.0)

    def testMinimoTriple(self):
        self.assertEqual(calcularNotaMinima(4.0, 4.0, 4.0), 4.0)

    def testMediaIguales(self):
        self.assertEqual(calcularNotaMedia(6.0, 6.0, 6.0), 6.0)


if __name__ == '__main__':
    unittest.main()
