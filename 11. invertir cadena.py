def inicio():
	print invertirCadena(raw_input("invertir cadena:\ningrese cadena: "))
	raw_input("enter para salir")

def invertirCadena(cad):
	if len(cad) == 1:
		return cad
	else:
		return invertirCadena(cad[1:]) + cad[0]
		
inicio()