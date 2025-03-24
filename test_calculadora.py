import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    def setUp(self):
        self.calc = Calculadora()

    def test_multiplicar_positivos(self):
        self.assertEqual(self.calc.multiplicar(2, 3), 6)

    def test_multiplicar_negativos(self):
        self.assertEqual(self.calc.multiplicar(-2, -3), 6)

    def test_multiplicar_mixto(self):
        self.assertEqual(self.calc.multiplicar(-2, 3), -6)

    def test_multiplicar_por_cero(self):
        self.assertEqual(self.calc.multiplicar(5, 0), 0)

if __name__ == "__main__":
    unittest.main()
