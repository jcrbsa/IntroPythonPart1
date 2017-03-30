while(True):

	numero_str = str(input("Digite um número inteiro:"))
	tam = len(numero_str)
	numero = int(numero_str)

	i =0 
	sinalizador = False
	anterior  = -numero

	while i  < tam and not sinalizador and tam > 1:
		
		atual = numero % 10
		numero = numero // 10
		
		if(anterior == atual):
			sinalizador = True
			
		anterior = atual 
		i = i + 1
		
		
	if(sinalizador):
		print("sim")
	else:
		print("não")
	
	
			
	
	
