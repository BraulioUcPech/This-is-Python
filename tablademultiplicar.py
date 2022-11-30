"""factor = 3  # factor deseado, en este caso, haremos la tabla del 5
desde = 1  # límite inferior (incluido)
hasta = 10  # límite superior (incluido también)

for f in range(desde, hasta + 1):
	print(f'{factor} x {f} =  {factor * f}')"""




tabla_desde = 1 #tablas del 1...
tabla_hasta = 20 #...al 10
desde = 1 #multiplicaciones desde el 1...
hasta = 10 #...hasta el 10

for factor1 in range(tabla_desde, tabla_hasta + 1):
	print(f'Tabla de multiplicar del {factor1}:') #mostramos una cabecera para cada tabla
	for factor2 in range(desde, hasta + 1):
		print(f'{factor1} x {factor2} = {factor1 * factor2}')
	print() #línea en blanco al final de cada tabla
