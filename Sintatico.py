def parse(self):
	apenArquivo()
	getToken()
	self.soma()
	consome(tkEOF)
	fechaAqrquivo()

def soma(self):
	#soma = mult resto soma
	self.mult()
	restoSoma()

def restoSoma():
	#restosoma = vazio | + mult resto soma | - mult resto soma
	if (Atual.token == tkmais):
		consome(tkmais)
		mult()
		restoSoma()
	elif (Atual.token == tkmenos):
		print("ident")
	else:
		pass

def consome(self):
	if(token == Atual.token):
		gettoken()
	else:
		print("ERRO: era esperado o token "+msg(token+", mas veio o token "+msg(Atual.token)+": linha "+Atual.linha+", coluna: "Atual.coluna+"\n"))

def fator(self):
	if (Atual.token == token.ident):
		if (Token.lexema in tabSimb):
			res = tabSimb[Atual.lexema]
		else:
			raise Exception("variavel nao declarada")
		consome(token.ident)
	elif(Atual.token === token.abrePar):
		consome(token.abrePar)
		res = soma()
		consome(token.fechaPar)
	else:
		if (Atual.token == token.num):
			res == int (Atual.lexema)
		consome(token.num)
	return res

def mult(self):
	uno()
	restoMult()

def restoMult(self):
	if(Atual.token == tkMult):
		consome(tkMult)
		uno()
		restoMult()
	elif(Atual.token == tkDiv):
		consome(tkDiv)
		uno()
	elif:
		pass

def uno(self):
	if(Atual.token == tkMais):
		consome(tkMais)
		uno()
	elif(Atual.token == tkMenos):
		consome(tkMenos)
		uno()
	else
		fator()
	
	
