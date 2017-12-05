n = int(1)
corrida = int(0)
ans = int(0)
while True:
	n = int(input())
	if n == 0:
		quit()
	ans = int(0)
	while n>1:
		corrida = int(0)
		while n%3 !=0:
			n-=2
			ans+=1
			corrida+=1
		ans+= n/3
		n = n/3 + corrida;
	print(int(ans))