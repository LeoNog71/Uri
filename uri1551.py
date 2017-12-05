import string
a = list(string.ascii_lowercase)

n = int(input())
i = int(0)


while i< n:
	
	s = str(input())
	t = int(0)
	
	for x in a:
		if s.find(x) >= 0:
			t+=1
	
	if t == len(a):
		print("frase completa")
	elif t >= len(a)/2 and t < len(a):
		print("frase quase completa")
	elif t < len(a)/2:
		print("frase mal elaborada")
	
	i+=1