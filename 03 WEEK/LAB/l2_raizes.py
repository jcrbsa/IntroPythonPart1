import math

a = float(input("Digite coeficiente a: "))
b = float(input("Digite coeficiente b: "))
c = float(input("Digite coeficiente c: "))


delta = (b ** 2 - 4 * a * c)

if delta < 0:
	print("esta equação não possui raízes reais")
else:
	raizquadradadelta = math.sqrt(delta)
	positivo = ( -b + raizquadradadelta) / (2 * a)
	if delta > 0:
		negativo =   (-b - raizquadradadelta) / (2 * a)
		print("as raízes da equação são", negativo, "e", positivo)
	else:
		print("a raiz desta equação é", positivo)
			 

			
		
