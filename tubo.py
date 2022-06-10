from dado import *
import random

'''
Classe responsável pelo Tubo com os 13 dados.
'''

class Tubo:

	# Inicializa o tubo com 13 dados, sendo 6 verdes, 4 amarelos e 3 vermelhos.
	def __init__(self):
		self.dados = []
		for i in range(6):
			self.dados.append(Dado(VERDE))
		for i in range(4):
			self.dados.append(Dado(AMARELO))
		for i in range(3):
			self.dados.append(Dado(VERMELHO))

	# Retira do tubo aleatoriamente a quantidade de dados desejada (qtd)
	def retirarDados(self, qtd):
		dados = []
		for i in range(qtd):
			dado = random.choice(self.dados)
			self.dados.remove(dado)
			dados.append(dado)
		return dados

	# Recoloca no tubo a lista de dados informado no parâmetro
	def colocarDados(self, dados):
		for dado in dados:
			self.dados.append(dado)

