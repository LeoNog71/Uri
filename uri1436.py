
t = int(input())
n = int()
x = []
i = int(0)
mediano= int()
while i <t:
	x = input().split(" ")
	
	sorted(x)
	mediano = int(len(x)/2)
	print("Case %d: %s"%(i+1,x[mediano]))
	i+=1
quit()