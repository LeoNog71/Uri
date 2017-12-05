i = int(0)
c = int(input())

while i<c:
	s= "N"
	p1 = input()
	p2 = input()
	p3 = input()
	j = int(0)
	temp = int(0)
	t = str()
	r = str()
	lista = []
	while j < len(p1):
		if p3[j] == "_":
			
			t = p1[j]
			r = p2[j]
			lista.append(p1[j])
			lista.append(p2[j])
			
			temp+=1
			if t==r:
				break
			else:
				if temp == 2:
					if lista[0] == lista[3] or lista[1] == lista[2]:
						s = "Y"
			#if p1[j] == p2[j]:
				
		
		j+=1
	print(s)
	i+=1


