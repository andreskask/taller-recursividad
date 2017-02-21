def inicio():
	if int(input("conversion de bases:\n1: decimal a binario\n2: binario a decimal\n")) == 1:
		print decimalBinario(int(input("ingrese decimal: ")))
	else:
		print binarioDecimal(int(input("ingrese binario: ")))
	raw_input("enter para salir")

def decimalBinario(numero):
    if numero == 0:
        return numero
    else:
        return (numero % 2) + 10 * decimalBinario(numero / 2)
 

def binarioDecimal(numero):
    if numero == 0:
        return numero
    else:
        return (numero % 10) + 2 * binarioDecimal(numero / 10)
		
inicio()