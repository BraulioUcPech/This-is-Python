""".Calcular e imprimir la tabla de multiplicar de un número cualquiera. Imprimir el 
multiplicando, el multiplicador y el producto.
"""


def main():

    numero = int(input("Ingrese el numero: "))

    for i in range(1, 11):
        print(numero, "x", i, "=", numero * i)

main()