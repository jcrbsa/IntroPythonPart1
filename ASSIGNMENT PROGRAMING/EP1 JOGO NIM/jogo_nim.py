

def computador_escolhe_jogada(n,m):

	#pecas_retiradas = 0
	#if( n % (m) == 0 and  (n/(m)) - ((n/(m))%10) == 0 ):
		
		#pecas_retiradas = m
	#else:	
	pecas_retiradas =  n% (m+1)
	
	if(pecas_retiradas == 0):
		pecas_retiradas = m
		
	if(pecas_retiradas == 1):
		print ("O computador tirou", pecas_retiradas ,  "uma peça.")
	else:
		print ("O computador tirou", pecas_retiradas ,  "peças.")

	return pecas_retiradas


def usuario_escolhe_jogada (n,m):
	
	pecas_retiradas = 0
	
	
	while (pecas_retiradas <= 0):
	
		print("Quantas peças você vai tirar?" )
		pecas_retiradas = int(input())
	
		if(pecas_retiradas > m ):
			print("Oops! Jogada inválida! Tente de novo.")		
			pecas_retiradas = 0

		
			
	if(pecas_retiradas == 1):
		print("Você tirou uma peça")
	else:
		print("Voce tirou", pecas_retiradas,"peças.")
			
	
	return pecas_retiradas
		

def partida():

	print("Voce escolheu uma partida!")

	num_pecas = 0
	limite_pecas = 1

	#while num_pecas < limite_pecas:
	print("Quantas peças? ")
	num_pecas = int(input())
	
	print("Limite de peças por jogada?")	
	limite_pecas = int(input())
	
	
	vez = 0
	pecas_retiradas = 0
	if(num_pecas % (limite_pecas+1) == 0):
		print("Voce comeca!")
		pecas_retiradas = usuario_escolhe_jogada(num_pecas,limite_pecas)
		vez = 1
		
	else:
		print("Computador comeca!")
		pecas_retiradas = computador_escolhe_jogada(num_pecas,limite_pecas)
		vez = 2
		
	num_pecas = num_pecas - pecas_retiradas
	
	if(num_pecas == 1):
			print("Agora resta apenas uma peça no tabuleiro.")
	elif(num_pecas > 1):
			print("Agora restam", num_pecas,"peças no tabuleiro.")

	while (num_pecas > 0 ):
		
		if (vez == 1):
			pecas_retiradas = computador_escolhe_jogada(num_pecas,limite_pecas)
			vez = 2			
		else:
			pecas_retiradas = usuario_escolhe_jogada(num_pecas,limite_pecas)
			vez = 1
			
		
		num_pecas = num_pecas - pecas_retiradas

		if(num_pecas == 1):
			print("Agora resta apenas uma peça no tabuleiro.")
		elif(num_pecas > 1):
			print("Agora restam", num_pecas,"peças no tabuleiro.")
		
	print("Fim de Jogo!")
	
	if(vez != 1):
		print("O computador ganhou!")
	else:
		print("Voce ganhou!")

	return vez
		
def campeonato():

	print("Voce escolheu um campeonato!")
	
	numero_partidas = 3
	i = 1 
	qt_vitorias_usuario = 0
	qt_vitorias_computador = 0
	vencedor_rodada = 0
	
	
	while(i<=numero_partidas):
		print("**** Rodada", i,"****")
		vencedor_rodada = partida()
		if(vencedor_rodada == 1):
			qt_vitorias_usuario = qt_vitorias_usuario + 1
		else:
			qt_vitorias_computador = qt_vitorias_computador + 1
		i = i + 1
	
	print("**** Final do campeonato! ****")
	print("Placar: Você", qt_vitorias_usuario  ,"X", qt_vitorias_computador ,"Computador")



def main():

	while(True):
	
		print("Bem-vindo ao jogo do NIM! Escolha:")
		print("1 - para jogar uma partida isolada")
		print("2 - para jogar um campeonato")

		entrada_usuario = int(input())
		
		if entrada_usuario == 1:
			partida()
		elif entrada_usuario == 2 :
			campeonato()
		else:
			print("Entrada Invalida")


main()