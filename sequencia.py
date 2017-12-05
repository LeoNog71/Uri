#voidcarro


vet = [0,1]
cont = int(1)
i = int(2)
ultimo = int()
penultimo = int()


	

while True:
	try:
		n = int(input())

		if n == 0 or n == 1:
			print(vet[n-1])
		else:
			while i <= n:
				ultimo = vet[i-1]
				penultimo = vet[i-2]
				if cont == 2:
					vet.append(ultimo*penultimo)
					cont = 1;
				else:
					vet.append(ultimo+penultimo)
					cont = 2
				i+=1
				

			print(vet[n-1])			
		
	except EOFError:
		quit()
