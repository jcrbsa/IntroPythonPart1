#l6_maior.py


def maior_elemento(lista):
	
	maior = lista[0]
	for i in range(len(lista)):
	
		if lista[i] >= maior :
			maior = lista [i]

		
	
	
	return maior
	
def main():
	n =1
	lista = []
	while(n > 0):
		n  = int(input("Digite um numero: "))
		if(n!=0):
			lista.append(n)
		
	print(maior_elemento(lista))	

		
main()