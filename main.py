from fraccion import Fraccion

def pedir_fraccion():
    entrada = input("Ingrese una fracción (ej: 3/4): ")
    num, den = map(int, entrada.split("/"))
    return Fraccion(num, den)

print("--- Calculadora de Fracciones ---")
f1 = pedir_fraccion()
f2 = pedir_fraccion()

print(f"Suma: {f1 + f2}")
print(f"Resta: {f1 - f2}")
print(f"Multiplicación: {f1 * f2}")
try:
    print(f"División: {f1 / f2}")
except ZeroDivisionError as e:
    print(e)

print("¿Son iguales?", f1 == f2)
print("Mayor:", max(f1, f2))

# Ordenar
lista = [Fraccion(3,4), Fraccion(1,2), Fraccion(2,3)]
ordenadas = sorted(lista)
print("Ordenadas:", ", ".join(str(f) for f in ordenadas))
