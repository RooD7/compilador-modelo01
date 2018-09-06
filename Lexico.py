class Token:
	abrePar 	= 1
	fechaPar 	= 2
	ponto 		= 3
	ptoVirg		= 4
	num			= 5
	ident		= 6		# Variavel
	strg		= 7
	soma		= 8
	mult		= 9
	div			= 10
	sub			= 11
	mod			= 12
	pot			= 13
	entrada		= 14
	saida		= 15
	eof			= 16
	erro		= 17

	msg = ('(',')','.',';','num','ident','str','+','*','/','-','%','^','input','output','eof','erro')

class Atual:
	linha	= 1
	coluna	= 1
	token	= ''
	lexema	= ''

class Arquivo:
	nome	= None
	arq		= None
	linha	= None
	cursor	= None

	def __init__(self, arq):
		self.arq = arq

	def getToken(self):
		estado = 1
		while(True):
			#print('Linha atual: ',Atual.linha)
			if self.arq is '':
				break
			else:
				car = self.arq[0]
				self.arq = self.arq[1:]
				
			print('CAR = ',car)
			Atual.lexema += car
			Atual.coluna += 1
			if(estado == 1):
				if(car == '\n'):
					Atual.linha += 1
				if(car in (' ','\n','\t')):
					continue
				elif('a' <= car.lower() <= 'z'):
					estado = 2
				elif('0' <= car <= '9'):
					estado = 4
			elif (estado == 2):
				# letra ou digito
				if(('a' <= car.lower() <= 'z') or ('0' <= car <= '9')):
					continue
				else:
					estado = 3
			elif (estado == 3):
				# atualiza o atual
				Atual.linha += 1
				# return identificador
				return Token.ident
			elif (estado == 4):
				if ('0' <= car <= '9'):
					continue
				if (car == '.'):
					estado = 6
				else:
					estado = 5
			elif (estado == 5):
				# atualiza o atual
				Atual.linha += 1
				# return num
				return Token.num
			elif (estado == 6):
				if ('0' <= car <= '9'):
					estado = 7
				else:
					estado = 8
			elif (estado == 7):
				if('0' <= car <= '9'):
					continue
				else:
					estado = 5
			elif (estado == 8):
				# atualiza o atual
				Atual.linha += 1
				# return erro
				return Token.erro
			elif (car == eof):
				return Token.eof

