"""Calcular el mayor de cuatro números enteros introducidos por teclado.

"""

def main():

    n = int(input("Ingrese la cantidad de numeros: "))
    menor = 0
    mayor = 0

    for i in range(n):
        numero = int(input("Ingrese un numero: "))
        if i == 0:
            menor = numero
            mayor = numero
        else:
            if numero > mayor:
                mayor = numero
            if numero < menor:
                menor = numero

    print("El menor numero es: ", menor)
    print("El mayor numero es: ", mayor)

main()
