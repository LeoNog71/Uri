#voidCarro
n = input()
n = int(n)
i = int(0)



while i<n:

	s1 = str(input())

	s2 = str(input())

	s3 = str(input())

	cont = int(0)
	cont2 = int(0)
	y = int(0)
	for x in s1:
		
		if s2[y] == x:
			cont+=1 
			
		y+=1
	y = int(0)
	for k in s1:
		if s3[y] == k:
			cont2+=1 
			
		y+=1

	

	print("Instancia",i+1)
	if cont == cont2:
		print("empate")
	elif cont > cont2:
		print("time 1")
	else:
		print("time 2")
	i=+1