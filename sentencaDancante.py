#voidCarro

def transforma_dançante(frase):
    frase_modificada = ""
    contador = 0
    for letra in frase:
        if letra == " ":
            frase_modificada += " "
        elif contador%2 == 0:
            contador += 1
            frase_modificada += letra.upper()
        else:
            contador -= 1
            frase_modificada += letra.lower()
    return frase_modificada

while True:
	
	try:
		print(transforma_dançante(input()))
	except EOFError:
		quit()
	