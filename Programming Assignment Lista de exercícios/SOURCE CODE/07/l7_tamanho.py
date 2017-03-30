def dimensoes(matriz):
	
	lines = len(matriz[:])
	columns = len(matriz[0][:])
	size =  str(lines) + "X" + str(columns)
	print(size)
	
	


	
def test_dimensoes():
	print("Test 1 -> [[1], [2], [3]]")
	dimensoes([[1], [2], [3]])
	print("Test 2 -> [[1, 2, 3], [4, 5, 6]]")
	dimensoes([[1, 2, 3], [4, 5, 6]])


test_dimensoes()