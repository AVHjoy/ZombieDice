import random

# tipo de faces
CEREBRO = "CEREBRO"
PASSOS = "PASSO"
TIRO = "TIRO"

# cores
VERDE = 'VERDE'
AMARELO = 'AMARELO'
VERMELHO = 'VERMELHO'

'''
Classe de Dado.
Contém atributos 'faces' e 'cor'.
'''
class Dado:
	# Inicializa um dado com a cor desejada.
	def __init__(self, cor): 
		self.cor = cor
		# Cria conjunto (tupla) de faces conforme a cor.
		if cor == VERDE:
			self.faces = (CEREBRO, CEREBRO, CEREBRO, PASSOS, PASSOS, TIRO)
		elif cor == AMARELO:
			self.faces = (CEREBRO, CEREBRO, PASSOS, PASSOS, TIRO, TIRO)
		else:
			self.faces = (CEREBRO, PASSOS, PASSOS, TIRO, TIRO, TIRO)		
		
	# Sorteia uma face do dado e a retorna.
	def sortearFace(self):
		return random.choice(self.faces)