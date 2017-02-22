def inicio():
	print "lista de menores: " + pedirListas(int(input("lista de menores:\ningrese cantidad de listas: ")))
	raw_input("enter para salir")

def pedirListas(numero):
	if numero == 0:
		return ""
	else:
		return menorDeLista(raw_input("ingrese lista: ")) + pedirListas(numero - 1)

def menorDeLista(lista):
	if len(lista) == 1:
		return lista
	elif int(lista[0]) > int(lista[1]):
		return menorDeLista(lista[1:])
	else:
		return menorDeLista(lista[0] + lista[2:])
			
inicio()