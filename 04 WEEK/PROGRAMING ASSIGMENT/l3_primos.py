while(True):

	numero = int(input("Digite um número inteiro:"))
	
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
			print("primo")
		else:
			print("não primo")
	else:
		print("não primo")
	
	
