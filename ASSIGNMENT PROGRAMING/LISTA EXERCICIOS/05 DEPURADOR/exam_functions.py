import math

def total_Caracteres (x, y, z):
    return len(x)+len(y)+len(z)

def suspense(x):
    return math.sqrt(x)
	
def main():
	print(suspense(0))
	print(total_Caracteres ("introduction", "python", "2017"))
		

	
main()