#voidCarro

int(input())
l = []
l = input().split(" ")
i = int(2)
t = [0,0,0,0]
for x in l:
	if int(x)%2 == 0:
		t[0]+=1
	if int(x)%3 == 0:
		t[1]+=1
	if int(x)%4 == 0:
		t[2]+=1
	if int(x)%5 == 0:
		t[3]+=1
	
for x in t:

	print(x,"Multiplo(s) de",i)
	i+=1