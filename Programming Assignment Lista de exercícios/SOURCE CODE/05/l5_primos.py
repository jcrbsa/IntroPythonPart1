def ePrimo(x):
	fator =2
	if (x == 2):
		return True

	while( x % fator != 0 and fator <= x/2):
		fator = fator + 1
		
	if x % fator  == 0:
		return False
	else:
		return True
	

def n_primos(numero):
	fator = 2
	qt_numero_primos = 0
	
	while (fator < numero ):
		
		if(ePrimo(fator)):
			qt_numero_primos = qt_numero_primos +1
			
		fator = fator + 1
		
	return qt_numero_primos	
	
n = 2
while n >= 2:
	n  = int(input("Digite um numero: "))
	print(n_primos(n))