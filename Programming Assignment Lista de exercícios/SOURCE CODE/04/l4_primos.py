def e_maior(x, y):

	if x >= y :
		return False
	elif x < y :
		return True	

def e_primo(numero):
	
	i = 1
	count = 0;
	nao_primo =False
	
	if numero > 1:
		while(i <= numero and not nao_primo):
			if numero % i == 0:
				count = count + 1
			
			if count > 2:
				nao_primo = True
			
			i = i +1
								
		if(not nao_primo):
			return True
		else:
			return False
	else:
		return False
	
def maior_primo(x):
	maior  = 2;
	i = 3	
	while i <= x :
		if e_primo(i):
			if e_maior(maior, i ):
				maior = i
		i = i + 2
		
	return maior

def test_maior_primo():
	assert maior_primo(100), 97
	assert maior_primo(7), 7
		
def main():
	x = int(input())
	print(maior_primo(x))

	
main()	
#test_maior_primo()