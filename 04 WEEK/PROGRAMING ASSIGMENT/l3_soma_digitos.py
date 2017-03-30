numero_str = str(input("Digite um número inteiro:"))
tam = len(numero_str)
numero = int(numero_str)

i =0 
soma = 0
while i  < tam:
	
	soma = soma + numero % 10
	numero = numero // 10
	i = i + 1
	
print(soma)
	
	
			
	
	
