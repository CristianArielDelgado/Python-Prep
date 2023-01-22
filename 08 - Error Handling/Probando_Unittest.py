#Probando Unittest (Caja Negra) con una suma.

"""
import unittest 
def suma (num1,num2):
    resultado = num1 + num2
    return resultado

print (suma(1,2))

class cajaNegra(unittest.TestCase):
    def test_suma (self):
        num1 = 20
        num2 = 25
    
        resultado = suma(num1, num2)
        
        self.assertEqual(resultado, 45)

unittest.main(argv=[''], verbosity=2, exit=False)
"""
def Factorial(numero):
    if (type(numero)!= int):
        return None
    elif (numero < 1):
        return None
    
    while numero>=1:
        cuenta = numero * Factorial(numero-1)
        numero-=1
        
    
    return numero

print(Factorial(4))