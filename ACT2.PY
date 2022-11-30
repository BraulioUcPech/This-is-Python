"""Realizar un programa que transforme todas las letras del alfabeto de mayúsculas a
minúsculas.
"""

def main():

    print("----------------------------------------------")
    print("ESCRIBA CUALQUIER PALABRA. MOSTRARA EN MAYUSCULAS Y MINUSCULAS")
    print("----------------------------------------------")

    print("Cuantas veces quiere que se repita el proceso?")
    print("----------------------------------------------")

    repeticiones = int(input("Ingrese el numero de repeticiones: "))
    for i in range(repeticiones):
        palabra = input("Ingrese la palabra: ")
        print(palabra.upper())
        print(palabra.lower())


main()
