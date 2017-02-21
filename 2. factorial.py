def inicio():
	print factorial(int(input("factorial:\ningrese numero: ")))
	raw_input("enter para salir")

def factorial(numero):
	if numero == 0:
		return 1
	else:
		return numero * factorial(numero - 1)
		
inicio()