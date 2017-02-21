def inicio():	
	print media(suma(int(input("media de dos numeros:\ningrese primer numero: ")), int(input("ingrese segundo numero: "))))
	raw_input("enter para salir")

def suma(numero1, numero2):
	if numero2 == 0:
		return numero1
	else:
		return suma(numero1 + 1, numero2 - 1)

def media(numero):
	if numero < 2:
		return 0
	else:
		return 1 + media(numero - 2)

inicio()