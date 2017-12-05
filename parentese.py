x  = []

while True:	
	try:
		
		abre = int(1)
		fecha = int(1)
		x = input()
		for num in x:
			if num == '(':
				abre += 1
			else :
				if num == ')':
					fecha += 1
			
		if abre > fecha or fecha > abre:
			print("incorrect")
		else:
			 if abre == fecha:
					print("correct")

	except EOFError :
		quit()