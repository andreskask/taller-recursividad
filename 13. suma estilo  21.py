def inicio():
	print "sumar estilo 21: "
	if puntaje(sumar(mazo(pedir(int(input("ingrese cantidad de cartas: ")))))) > 21:
		print "perdiste "
	else:
		print "ganaste"
	raw_input("enter para salir")

def pedir(numero):
	if numero == 0:
		return ""
	else:
		return raw_input("ingrese carta: ") + pedir(numero - 1)

def sumar(carta):
	if len(carta) == 1:
		if carta[0] == 'j' or carta[0] == 'q' or carta[0] == 'k': 
			return 10
		elif carta[0] == "a":
			return 1
		else:
			return int(carta[0])			
	elif carta[0] == 'j' or carta[0] == 'q' or carta[0] == 'k': 
		return 10 + sumar(carta[1:])
	elif carta[0] == "a":
		return 1 + sumar(carta[1:])
	else:
		return int(carta[0]) + sumar(carta[1:])
		
def mazo(mazo):
	print "su mazo es: " + mazo
	return mazo
	
def puntaje(suma):
	print "su puntaje es: " + str(suma)
	return suma

inicio()