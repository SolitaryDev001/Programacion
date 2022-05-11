# 4. Se necesita un programa que permita ingresar la siguiente información de 
# N trabajadores de una empresa: 
# nombre, --> Listo
# edad (generada en forma aleatoria en el  rango 18 a 80 años), 
# tipo de contrato (Licenciado, Técnico u Obrero en forma aleatoria) y 
# la cantidad de horas trabajadas. --> Listo
# El valor de la hora depende del tipo 
# de contrato según tabla:
# Tipo de contrato	Valor hora
# Licenciado	$10250
# Técnico	$7120
# Obrero	$5200

# El programa debe mostrar:
# •	Edad, tipo de contrato y Sueldo de cada trabajador (valor hora x 
# cantidad de horas trabajadas) --> En el ciclo principal ---> lista
# •	Nombre y Edad del trabajador con mayor sueldo --> al final
# •	Total pagado por parte de la empresa a sus trabajadores --> al final -->Listo
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

# variables para la estadistica:
contador_mayores60 = 0
suma_sueldos = 0
mayor_sueldo = 0
nombre_mayor_sueldo = ""
edad_mayor_sueldo = 0


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
			horas_trabajadas = int(input("Ingrese el número horas trabajadas : "))
			if(horas_trabajadas > 0):
				valido = True
			else:
				print("El numero debe ser entero y positivo ")
		except ValueError: #en caso de que el try no se pueda hacer
			print("Error, debe ingresar un numero entero y positivo")


	# Generamos al azar la edad y el tipo de contrato :
	edad = random.randint(18,80)
	tipo_contrato = random.randint(1,3)
	# Asignamos el contrato y valor hora correspondiente
	contrato = ""
	valor_hora = 0
	if tipo_contrato == 1 :
		contrato = "Licenciado"
		valor_hora = 10250 
	elif tipo_contrato == 2  :
		contrato = "Tecnico"
		valor_hora = 7120
	elif tipo_contrato == 3  :
		contrato = "Obrero"
		valor_hora = 5200
	# calculamos cuanto hay que pagarle	
	sueldo = horas_trabajadas * valor_hora
	# imprimir los detalles del trabajador:
	print("nombre : " , nombre)
	print("edad : " , edad)
	print("tipo contrato : " , tipo_contrato)
	print("contrato : " , contrato)
	print("valor hora : ", valor_hora )
	print("horas trabajadas :" , horas_trabajadas )
	print("sueldo : " , sueldo)

	# actualizamos los valores para la estadistica. 
	suma_sueldos = suma_sueldos + sueldo
	if edad > 60 :
		contador_mayores60 = contador_mayores60 + 1
	if sueldo > mayor_sueldo :
		mayor_sueldo = sueldo
		edad_mayor_sueldo = edad
		nombre_mayor_sueldo = nombre

	# aumento el contador para continuar el ciclo principal
	contador_trabajadores = contador_trabajadores + 1

# -----------------------------------------------------------
# Parte 3 : Mostrar el resultado.
# -----------------------------------------------------------
print("La suma de los sueldos es : $" , suma_sueldos)
print("Hay  " , contador_mayores60 , " trabajadores mayores de 60 años")
print("El trabajador con mayor sueldo es : " , nombre_mayor_sueldo )
print("Y su edad es ", edad_mayor_sueldo)
