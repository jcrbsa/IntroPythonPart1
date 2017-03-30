
def sao_multiplicaveis(matriz1,matriz2):
	
	lines1 = len(matriz1[:])
	columns1 = len(matriz1[0][:])
	
	lines2 = len(matriz2[:])
	columns2 = len(matriz2[0][:])
	
	if(columns1 == lines2):
		return True
	else:
		return False
		
	
		


	
def test_imprime():
	print("Test 1 -> [[1], [2], [3]]")
	m1 = [[1, 2, 3], [4, 5, 6]]
	m2 = [[2, 3, 4], [5, 6, 7]]
	print(sao_multiplicaveis(m1,m2))
	
	print("Test 2 -> [[1, 2, 3], [4, 5, 6]]")
	m1 = [[1], [2], [3]]
	m2 = [[2, 3, 4]]
	print(sao_multiplicaveis(m1,m2))


test_imprime()