import unittest
from calculadora import Calculadora


class TestCalculadora(unittest.TestCase):

    def test_sumar(self):
        self.assertEqual(Calculadora.sumar(2, 3), 5)

    def test_sumar_texto(self):
        with self.assertRaises(ValueError):
            Calculadora.sumar("a", 3)


if __name__ == '__main__':
    unittest.main()