
while True:
	try:
		s = str(input())
		s2 = str(input())
		cont = int(0)

		for i in s:
			for j in s2:
				if i == j:
					cont+=1
		
		print(cont)
	except EOFError:
		quit()