#voidCarro
n = int(input())
i = int(0)



while i<n:

	s = str(input())

	if s.startswith('o') and s.endswith('e'):
		print(1)
	elif s.startswith('on'):
		print(1)
	elif s.endswith('ne'):
		print(1)
	elif s.startswith('t') and s.endswith('o'):
		print(2)
	elif s.startswith('tw'):
		print(2)
	elif s.endswith('wo'):
		print(2)
	elif s.startswith('th') and s.endswith('ee'):
		print(3)
	elif s.startswith('thr'):
		print(3)
	elif s.endswith('hree'):
		print(3)
	elif s.startswith('t') and s.endswith('ree'):
		print(3)

	i+=1
