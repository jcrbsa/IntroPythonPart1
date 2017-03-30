



def fizzbuzz(x):


	if x % 3 == 0 and x % 5 == 0 :
		return "FizzBuzz"
	elif x % 3 == 0 :
		return "Fizz"	
	elif x % 5 == 0 :
		return "Buzz"
	else:
		return x


def test_fizzbuzz():
	assert fizzbuzz(3), "Fizz" 
	assert fizzbuzz(5), "Buzz" 
	assert fizzbuzz(15),"FizzBuzz" 
	assert fizzbuzz(4), 4
		
		
def main():
	numero = int(input())
	print(fizzbuzz(numero))

	
main()	
#test_fizzbuzz()