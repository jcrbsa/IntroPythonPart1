#l6_repetidos.py


def remove_repetidos(lista):
	
	for i in lista:
		repeat = lista.count(i)
		if(repeat > 1):
			j = repeat
			while j >1:
				lista.remove(i)		
				j = j - 1
				
			
	return sorted(lista)
	
	
def test():
	
	assert remove_repetidos([1,2,3]), [1,2,3]
	assert remove_repetidos([1,2,1,3,4,7,10]), [1,2,1,3,4,7,10]
	assert remove_repetidos([7,3,33,12,3,3,3,7,12,100]), [3,7,12,33,100]
	assert remove_repetidos([1,1,1, 8,7,6,5,4,3, 2, 1,9]), [1, 2, 3, 4, 5, 6, 7, 8, 9]
	assert remove_repetidos([1,1,1, 8,7,6,5,4,3, 2, 1,9,9,9]), [1, 2, 3, 4, 5, 6, 7, 8, 9]
	assert remove_repetidos([1,1,1, 8,7,6,5,5,5,4,4,3, 2, 1,9]), [1, 2, 3, 4, 5, 6, 7, 8, 9]
	assert remove_repetidos([1,1,1]), [1]
	
	
def main():
	n =1
	lista = []
	while(n > 0):
		n  = int(input("Digite um numero: "))
		if(n!=0):
			lista.append(n)
		
	print(remove_repetidos(lista))	

#test()
main()