def inicio():
	print valorAbsoluto(int(input("valor absoluto:\ningrese numero: ")))
	raw_input("enter para salir")

def valorAbsoluto(numero):
	if numero > 0:
		return numero
	else:
		return valorAbsoluto(-numero)
		
inicio()