
def maximo(x, y, z):

	if x >= y and x >= z :
		return x
	elif y >= x and y >= z :
		return y	
	elif z >= x and z >= y :
		return z
	
def test_maximo():
	assert maximo(30,14,10), 30
	assert maximo(0,-1,1), 1
		
def main():
	x = int(input())
	y = int(input())
	z = int(input())
	print(maximo(x,y,z))

	
main()	
#test_maximo_3()