import math
from math import sqrt
class Complejo(object):

    def __init__(self, real, imag=0.0):
        self.real = real
        self.imag = imag
        print(self.real + self.imag)

    def __add__(self, other):
        print('\nSuma:')
        return Complejo(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        print('\nResta:')
        return Complejo(self.real - other.real, self.imag - other.imag)
    
    def __mul__(self, other):
        print('\nProducto:')
        return Complejo((self.real * other.real - self.imag * other.imag),
            (self.real * other.imag + self.imag * other.real))

    def __truediv__(self, other):
        print('\nCuociente:')
        r = (other.real**2 + other.imag**2)
        return Complejo((self.real*other.real - self.imag*other.imag)/r,
            (self.imag*other.real + self.real*other.imag)/r)

i = Complejo(2, 10j)
k = Complejo(3, 5j)

# Sumar
i + k
# Restar
i - k
# Multiplicar
i * k
# Dividir
i / k

