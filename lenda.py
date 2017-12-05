x = []
y = int()
z = int()

n = int(input())
i  =int(0)

while i < n:
	x = []
	y,z = input().split(" ")
	y = int(y)
	z = int(z)
	for j in y:
		x.append(j)

	a = x
	b = z-1
	while len(x) != 1:
		if b > len(x):
			b %= z-1
		del x[b]
		b+= z-1

	print(i+1," >", x)
	i+=1