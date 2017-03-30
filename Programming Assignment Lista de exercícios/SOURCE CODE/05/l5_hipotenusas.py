
def e_hipotenusa(x):
	
	hipotenusa = x ** 2
	parada = x ** 2
	i = 1
	while (i <= parada):
		j = i
		while(j >= 1):

			soma_catetos = i ** 2 + j ** 2
			if(soma_catetos == hipotenusa):
				return True
				
			j = j - 1
			
		i = i + 1
		
	
	return False

		
	

def soma_hipotenusas(numero):
	fator = 1
	qt_numero_primos = 0
	
	while (fator <= numero ):
	
		if (e_hipotenusa(fator)):
			print(fator,  end = " ")
			qt_numero_primos = qt_numero_primos + fator
			
		fator = fator + 1
	
	print("Soma Total: ", qt_numero_primos)
	return qt_numero_primos	

def test_soma_hipotenusas():
	assert soma_hipotenusas(5),5
	assert soma_hipotenusas(6),5
	assert soma_hipotenusas(10),15
	assert soma_hipotenusas(11),15
	assert soma_hipotenusas(13),28
	assert soma_hipotenusas(14),28
	assert soma_hipotenusas(15),43
	assert soma_hipotenusas(16),43
	assert soma_hipotenusas(17),60
	assert soma_hipotenusas(18),60
	assert soma_hipotenusas(20),20
	assert soma_hipotenusas(21),20
	assert soma_hipotenusas(25),105
	assert soma_hipotenusas(26),105	

	
def main():
	n = 1
	while n >= 1:
		n  = int(input("Digite um numero: "))
		print(n_primos(n))
	print(0)


main()
#test_soma_hipotenusas()

