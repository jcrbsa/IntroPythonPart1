#l6_inverte.py

def main():
	n =1
	lista = []
	while(n > 0):
		n  = int(input("Digite um numero: "))
		if(n!=0):
			lista.append(n)
		
	i = len(lista)-1
	while i >= 0:
		print(lista[i]) 
		i = i - 1

		
main()
	 