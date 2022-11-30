"""i Algoritmo que lea un número entero (lado) y a partir de él cree un cuadrado de
asteriscos con ese tamaño. Los asteriscos sólo se verán en el borde del cuadrado, no en el interior.
Ejemplo, para lado = 4 escribiría:s"""


def main():

    lado = int(input("Ingrese el lado del cuadrado: "))

    for i in range(lado):
        for j in range(lado):
            if i == 0 or i == lado - 1 or j == 0 or j == lado - 1:
                print("*", end="")
            else:
                print(" ", end="")

main()


