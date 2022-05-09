# 4. Se necesita un programa que permita ingresar la siguiente información de 
# N trabajadores de una empresa: 
# nombre, --> Listo
# edad (generada en forma aleatoria en el  rango 18 a 80 años), 
# tipo de contrato (Licenciado, Técnico u Obrero en forma aleatoria) y 
# la cantidad de horas trabajadas. 
# El valor de la hora depende del tipo 
# de contrato según tabla:
# Tipo de contrato	Valor hora
# Licenciado	$10250
# Técnico	$7120
# Obrero	$5200

# El programa debe mostrar:
# •	Edad, tipo de contrato y Sueldo de cada trabajador (valor hora x 
# cantidad de horas trabajadas) --> En el ciclo principal???
# •	Nombre y Edad del trabajador con mayor sueldo --> al final
# •	Total pagado por parte de la empresa a sus trabajadores --> al final
# •	Cantidad trabajadores con más de 60 años --> al final

# Mi problema tiene tres partes: 
# 1 - preparacion inicial
# 2 - ciclo principal
# 3 - mostrar resultados resumidos

# -----------------------------------------------------------
# Parte 0 : importar lo que necesitemos 
# -----------------------------------------------------------
import os;
import random;

# -----------------------------------------------------------
# Parte 1 : preparación: preguntar cuantos trabajadores hay
# -----------------------------------------------------------
os.system('cls')
# ingreso con validacion
valido = False
while(not valido ): # mientras el ingreso no sea valido 
	try:
		n = int(input("Ingrese el número de trabajadores : "))
		if(n > 0):
			valido = True
		else:
			print("El numero debe ser entero y positivo ")
	except ValueError: #en caso de que el try no se pueda hacer
			print("Error, debe ingresar un numero entero y positivo")

print('Hay ' , n , ' trabajadores')


# -----------------------------------------------------------
# Parte 2 : ciclo principal...
# -----------------------------------------------------------
contador_trabajadores = 0
while(contador_trabajadores < n ) :
	# Leemos el nombre con validacion.
	nombre = ""
	while(len(nombre)==0) :
		nombre = input("Ingrese el nombre del trabajador : ")
		if (len(nombre) == 0):
			print("El nombre no puede quedar vacio.")
			
	# Leemos la cantidad de horas trabajadas: 
	valido = False
	while(not valido ): # mientras el ingreso no sea valido 
		try:
			n = int(input("Ingrese el número horas trabajadas : "))
			if(n > 0):
				valido = True
			else:
				print("El numero debe ser entero y positivo ")
		except ValueError: #en caso de que el try no se pueda hacer
			print("Error, debe ingresar un numero entero y positivo")

	# continuamos con el proceso:
	print("nombre : " , nombre)
	contador_trabajadores = contador_trabajadores + 1
