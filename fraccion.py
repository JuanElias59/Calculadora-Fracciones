from math import gcd

class Fraccion:
    def __init__(self, numerador, denominador):
        if denominador == 0:
            raise ZeroDivisionError("Denominador no puede ser cero.")
        self.numerador = numerador
        self.denominador = denominador
        self.simplificar()

    def simplificar(self):
        mcd = gcd(self.numerador, self.denominador)
        self.numerador //= mcd
        self.denominador //= mcd

    def __add__(self, other):
        num = self.numerador * other.denominador + other.numerador * self.denominador
        den = self.denominador * other.denominador
        return Fraccion(num, den)

    def __sub__(self, other):
        num = self.numerador * other.denominador - other.numerador * self.denominador
        den = self.denominador * other.denominador
        return Fraccion(num, den)

    def __mul__(self, other):
        return Fraccion(self.numerador * other.numerador, self.denominador * other.denominador)

    def __truediv__(self, other):
        if other.numerador == 0:
            raise ZeroDivisionError("No se puede dividir por cero.")
        return Fraccion(self.numerador * other.denominador, self.denominador * other.numerador)

    def __eq__(self, other):
        return self.numerador * other.denominador == other.numerador * self.denominador

    def __lt__(self, other):
        return self.numerador * other.denominador < other.numerador * self.denominador

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"
