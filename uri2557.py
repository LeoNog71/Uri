x = str()
y = str()
while True:
	try:
		x = str()
		y = str()
		y,x = input().split("=")
		
		y=y.split("+")
		if x == "J":
			print(int(y[0])+int(y[1]))
		else :
			if y[1] == "L":
				print(int(x)-int(y[0]))
			else:
				if y[0] == "R":
					print(int(x)-int(y[1]))
	except EOFError :
		quit()
		