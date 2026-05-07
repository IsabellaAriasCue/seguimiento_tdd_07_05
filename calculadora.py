class Calculadora:

    @staticmethod
    def sumar(a, b):

        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Los valores deben ser numéricos")

        return a + b