
def imprime_matriz(matriz):
	for i in range(len(matriz[:])):	
		temp = ""
		for j in range(len(matriz[i][:])):
			if( j == len(matriz[i][:]) -1):
				temp = temp + str(matriz[i][j])
				
			else:
				temp = temp + str(matriz[i][j]) + " "
		print(temp)
	


	
def test_imprime():
	print("Test 1 -> [[1], [2], [3]]")
	imprime_matriz([[1], [2], [3]])
	print("Test 2 -> [[1, 2, 3], [4, 5, 6]]")
	imprime_matriz([[1, 2, 3], [4, 5, 6]])


test_imprime()