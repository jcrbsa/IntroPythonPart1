
largura  = int(input("digite a largura:"))
altura = int(input("digite a altura:")) 
i =1 

while (i <= altura):
	j = 1
	while(j <= largura):
		
		if(i == 1 or i == altura):
			print("#", end = "")
		else:
			if ((j > 1 and j < largura)): 
				print(" ", end = "")
			else:
				print("#", end = "")
				
			
		j = j + 1
	print()
	i = i + 1