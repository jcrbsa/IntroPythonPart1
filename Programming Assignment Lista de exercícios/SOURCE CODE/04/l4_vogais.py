
def vogal(x):
	x = x.lower()
	if x == "a" or x == "e" or  x == "i" or x == "o" or x == "u" :
		return True
	return False
 	
def test_vogal():
	assert vogal("a"), True
	assert vogal("E"), True
	assert vogal("b"), False
		
def main():
	x = str(input())	
	print(vogal(x))

	
main()	
#test_vogal()