while True:
	try:
		lista = []
		cont = int(0)
		n = int(input())
		i = int(0)
		j = int(0)
		str3 = str()
		while i < n:
			if i == 0:
				string = input()
				str2 = string
			else:
				string = input()
				for x in str2:
					if x == string[j]:
						cont+=1
					else:
						if x == str3[j]:
							cont+=1
					j+=1
				j = 0
				str3 = str2
				str2 = string

			i+=1
		
		if n>2:

			print(cont- n)
		else:
			print(cont)
	except EOFError :
		quit()