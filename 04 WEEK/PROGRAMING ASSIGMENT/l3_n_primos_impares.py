numero = int(input("Digite o valor de n:"))
x = 1
temp = 1
while x <= numero:
	i = 1
	count = 0;
	nao_primo =False
	
	while(i <= temp and not nao_primo):
		if temp % i == 0:
			count = count + 1
		
		if count > 2:
			nao_primo = True
		
		i = i +2
		
	if not nao_primo:
		print(temp)
		
	temp = temp + 2
	x= x + 1
		
	
	
