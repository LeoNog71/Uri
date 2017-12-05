#voidCarro
m = int(1)
n = int(2)
string = str()
while True:
	
	m,n = input().split()

	m = int(m)
	n = int(n)

	if m ==0 and n ==0 and m == n:
		quit()

	string = str(n+m)

	for x in string:
		
		string = string.replace("0","")

	print(string)
