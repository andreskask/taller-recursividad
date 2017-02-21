def inicio():
	print fib(int(input("sucesion de fibonacci:\ningrese numero: ")))
	raw_input("enter para salir")

def fib(numero):
    if numero < 3:
        return 1
    else:
		return fib(numero - 1) + fib(numero - 2)
		
inicio()