def inicio():
	print potencia(int(input("potencia:\ningrese base: ")), int(input("ingrese exponente: ")))
	raw_input("enter para salir")

def potencia(base, exp):
	if exp == 0:
		return 1
	else:
		return base * potencia(base, exp - 1)
		
inicio()