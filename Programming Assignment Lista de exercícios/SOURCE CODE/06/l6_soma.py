#l6_soma.py


def soma_elementos(lista):
	soma = 0
	
	for i in range(len(lista)):
		soma = soma + lista[i]
	
	
	return soma
	
def main():
	n =1
	lista = []
	while(n > 0):
		n  = int(input("Digite um numero: "))
		if(n!=0):
			lista.append(n)
		
	print(soma_elementos(lista))	

		
main()