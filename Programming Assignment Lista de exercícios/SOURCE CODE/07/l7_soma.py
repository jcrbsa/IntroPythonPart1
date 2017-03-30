
def soma_matrizes(matriz1, matriz2):
	lines1 = len(matriz1[:])
	columns1 = len(matriz1[0][:])
	
	lines2 = len(matriz2[:])
	columns2 = len(matriz2[0][:])
	
	if columns1 != columns2 or lines1 != lines2 :
		return False
	else:
		matriz_soma = []
		for i in range(len(matriz1[:])):	
			linha =  [];
			for j in range(len(matriz1[i][:])):
				linha.append(matriz1[i][j] + matriz2[i][j])
			
			matriz_soma.append(linha)
	
		return matriz_soma

	
def test_imprime():
	print("Test 1 -> [[1], [2], [3]]")
	m1 = [[1, 2, 3], [4, 5, 6]]
	m2 = [[2, 3, 4], [5, 6, 7]]
	print(soma_matrizes(m1,m2))
	
	print("Test 2 -> [[1, 2, 3], [4, 5, 6]]")
	m1 = [[1], [2], [3]]
	m2 = [[2, 3, 4], [5, 6, 7]]
	print(soma_matrizes(m1,m2))



test_imprime()