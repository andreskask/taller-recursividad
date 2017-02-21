def inicio():
	print division(int(input("division:\ningrese dividendo: ")), int(input("ingrese divisor: ")))
	raw_input("enter para salir")

def division(numero1, numero2):
	if numero1 < numero2:
		return 0
	else:
		return 1 + division(numero1 - numero2, numero2)
		
inicio()