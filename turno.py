import time # para uso da função sleep()
from dado import * # importa a classe Dado

'''
Classe responsável por controlar um turno de um jogador.
Contém apenas o método 'jogarDados' e os atributos necessários para controlar um turno.
'''

class Turno:

	# Lista de dados que estão com o jogador no turno.
	def __init__(self):
		self.dadosCerebro = []
		self.dadosPassos = []
		self.cerebros = 0
		self.tiros = 0

	# Obtém a lista de dados a serem jogados (dados de passos + dados do tubo que precisarem)
	def __obterListaDadosJogar(self, tubo):
		# Inicializa lista de dados que serão jogados.
		dadosJogar = []		
		# Adiciona os dados de passos na lista de dados a serem jogados.
		for dado in self.dadosPassos:
			dadosJogar.append(dado)
		# Zera a lista de passos, pois já adicionou os dados de passos na lista a ser jogada.
		self.dadosPassos = []
		# Adiciona os dados retirados do tubo para completar 3 dados.
		for dado in tubo.retirarDados(3 - len(dadosJogar)):
			dadosJogar.append(dado)
		# Retorna a lista de dados.
		return dadosJogar

	# Se o tubo tiver menos que 3 dados, joga os dados de cérebro de volta no tubo.
	def __corrigirTubo(self, tubo):
		if len(tubo.dados) < 3:
			print("Devolvido(s)", len(self.dadosCerebro), "dado(s) de cérebro(s) ao tubo.")
			time.sleep(1)
			tubo.colocarDados(self.dadosCerebro)
			self.dadosCerebro = []		

	# Joga 3 dados e computa o resultado no turno
	def jogarDados(self, tubo):
		# Se o tubo tiver menos que 3 dados, joga os dados de cérebro de voltam ao tubo.
		self.__corrigirTubo(tubo)
		# Inicializa lista de dados que serão jogados.
		dadosJogar = self.__obterListaDadosJogar(tubo)
		# sorteia e computa cada um dos 3 dados
		print("Dados sorteados: ", end="")
		for dado in dadosJogar:
			face = dado.sortearFace()
			print(f"[{face} {dado.cor}]", end=" ")
			if face == CEREBRO:
				self.cerebros += 1 # computa um cérebro para o turno do jogador
				self.dadosCerebro.append(dado)
			elif face == PASSOS:
				self.dadosPassos.append(dado)
			else: # face == TIROS
				self.tiros += 1
		print("")
		time.sleep(1)
