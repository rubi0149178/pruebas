# -*- coding: utf-8 -*-
import unittest
import sys

# Lógica de la calculadora
class Calculator:
    """Una clase simple para realizar operaciones aritméticas básicas."""

    def add(self, a, b):
        """Suma dos números."""
        return a + b

    def subtract(self, a, b):
        """Resta dos números."""
        return a - b

    def multiply(self, a, b):
        """Multiplica dos números."""
        return a * b

    def divide(self, a, b):
        """Divide el primer número por el segundo. Levanta ValueError si se divide por cero."""
        if b == 0:
            raise ValueError("No se puede dividir por cero.")
        return a / b

# Implementación de Pruebas Unitarias
# Se puede ejecutar con 'python -m unittest calculator.py'

class TestCalculator(unittest.TestCase):
    """Pruebas unitarias para la clase Calculator."""

    def setUp(self):
        """Configura una nueva instancia de Calculator antes de cada prueba."""
        self.calc = Calculator()

    # 1. Prueba Unitaria Requerida: Suma Correcta
    def test_add_correct(self):
        """Verifica que el método add() devuelva la suma correcta de dos números positivos."""
        self.assertEqual(self.calc.add(10, 5), 15, "Debería ser 15")

    # Prueba Unitaria Adicional: Manejo de error de división
    def test_divide_by_zero(self):
        """Verifica que dividir por cero levante la excepción esperada."""
        # Se usa assertRaises para verificar que se levante la excepción ValueError
        with self.assertRaisesRegex(ValueError, "No se puede dividir por cero."):
            self.calc.divide(10, 0)

# Si se ejecuta este archivo directamente, se ejecutan las pruebas.
if __name__ == '__main__':
    print("Ejecutando pruebas unitarias...")
    # Ejecutamos las pruebas unitarias
    # Usamos argv para evitar que unittest.main() intente analizar argumentos de la línea de comandos en este entorno
    unittest.main(argv=sys.argv[:1], exit=False)
    
    print("\n--- Ejemplo de uso de la calculadora ---")
    c = Calculator()
    print(f"15 + 7 = {c.add(15, 7)}")
    print(f"20 / 4 = {c.divide(20, 4)}")
    try:
        c.divide(10, 0)
    except ValueError as e:
        print(f"Error de división: {e}")

