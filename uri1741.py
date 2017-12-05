
while True:
	try:
		x = str()
		resultado = float()
		exp = str()
		y = []
		x = input().split()
		if x[0] != "+" or x[0] != "-" or x[0] != "*" or x[0] != "/":
			print("Invalid expression.")
		else:
			x = x[::-1]
			for j in x:
				y.append(j)
				y.append(j+2)
			while i < len(y):
				if y[i] == "+":
				else:
					if y[i] == "-":
					else:
						if y[i] == "*":
						else:
							if y[i] == "/":
							else:
								


		
	except EOFError :
		quit()
		