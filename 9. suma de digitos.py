def inicio():	
	print sumaDigitos(raw_input("suma de digitos:\ningrese numero: "))
	raw_input("enter para salir")

def sumaDigitos(numero):
	if len(numero) < 2:
		return int(numero)
	else:
		return int(numero[len(numero) - 1]) + sumaDigitos(numero[:-1])
		
inicio()