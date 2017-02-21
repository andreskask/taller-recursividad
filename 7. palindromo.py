def inicio():	
	if palindromo(raw_input("palindromo:\ningrese algun texto: ")):
		print "es palindromo"
	else:
		print "no es palindromo"
	raw_input("enter para salir")

def palindromo(cad):
    if len(cad) < 2:
		return True
    if cad[0] != cad[-1]:
		return False
    return palindromo(cad[1:-1])

inicio()