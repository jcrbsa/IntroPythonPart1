



def maximo(x, y):


	if x >= y :
		return x
	elif x < y :
		return y	
	


def test_maximo():
	assert maximo(3,4), 4
	assert maximo(0,0), 0
		
def main():
	x = int(input())
	y = int(input())
	print(maximo(x,y))

	
main()	
#test_maximo()