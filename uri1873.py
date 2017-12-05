#voidCarro
n = int(input())
i = int(0)

while i<n:
	r,s = input().split(" ")

	if r == 'tesoura' and s == 'papel':
		print("rajesh")
	elif s == 'tesoura' and r == 'papel':
		print("sheldon")
	
	elif r == 'papel' and s == 'pedra':
		print("rajesh")
	elif s == 'papel' and r == 'pedra':
		print("sheldon")
	
	elif r == 'pedra' and s == 'lagarto':
		print("rajesh")
	elif r == 'lagarto' and s == 'pedra':
		print("sheldon")
	
	elif r == 'lagarto' and s == 'spock':
		print('rajesh')
	elif r == 'spock' and s == 'lagarto':
		print('sheldon')

	elif r == 'spock' and s == 'tesoura':
		print('rajesh')
	elif r == 'tesoura' and s =='spock':
		print('sheldon')
	
	elif r == 'tesoura' and s =='lagarto':
		print('rajesh')
	elif r == 'lagarto' and s == 'tesoura':
		print('sheldon')

	elif r == 'lagarto' and s == 'papel':
		print('rajesh')
	elif r == 'papel' and s == 'lagarto':
		print('sheldon')

	elif r == 'papel' and s == 'spock':
		print('rajesh')
	elif r == 'spock' and s == 'papel':
		print('sheldon')

	elif r == 'spock' and s == 'pedra':
		print('rajesh')
	elif r == 'pedra' and s =='spock':
		print('sheldon')

	elif r == 'pedra' and s =='tesoura':
		print('rajesh')
	elif r ==  'tesoura' and s == 'pedra':
		print('sheldon')

	elif r == s:
		print('empate')

	i+=1

