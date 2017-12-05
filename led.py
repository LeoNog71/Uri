#voidCarro

x = []

n = int(input())
i = int(0)
soma = int()

while i < n:
	soma = int(0)
	x =[]
	x = str(input())
	for j in x:
		if j == '1':
			soma += 2
		if j == '2':
			soma += 5
		if j == '3':
			soma += 5
		if j == '4':
			soma += 4
		if j == '5':
			soma += 5
		if j == '6':
			soma += 6
		if j == '7':
			soma+= 3
		if j == '8':
			soma += 7
		if j == '9':
			soma += 6
		if j == '0':
			soma += 6
	print(soma, "leds")
	i+=1


