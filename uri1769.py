x =[]
y = [1,2,3,0,4,5,6,0,7,8,9]
b1 = int()
b2 =  int()
test = int(0)
j = int(0)
i = int(10)
resultado = int(0)
while True:
	try:
		x =[]
		b1 = int(0)
		b2 =  int(0)
		test = int(0)
		resultado = int(0)
		j = int(0)
		i = int(10)
		x = input()
		while j < 11:
			if j == 3 or j == 7:
				pass
			else:
				resultado += int(x[j])*y[j]
				
			j+=1
		if resultado % 11 == 10:
			b1 = 0
		else:
			b1 = resultado % 11
		
		if b1 == int(x[12]):
			test +=1
		
		j = int(0)
		resultado = int(0)
		while j < 11:
			if j == 3 or j == 7:
				pass
			else:
				resultado += int(x[j])*y[i]
				
			j+=1
			i-=1
		
		if resultado % 11 == 10:
			b2 = 0
		else:
			b2 = resultado % 11
		
		if b2 == int(x[13]):
			test += 1
		
		if test == 2:
			print("CPF valido")
		else:
			print("CPF invalido")

	except EOFError :
		quit()
