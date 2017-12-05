
x = []
s = str()
while True:
	

	x = []
	
	m = str()
	x = input().split(" ")
	if x == '0':
		break
	for i in x:
		s += str(len(i))+"-"
		if len(m) < len(i):
			m = i

	n = len(s)
	del s[n-1]
	print(s)

print("The biggest word:",m)	

		