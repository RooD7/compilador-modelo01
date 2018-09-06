def parse(self):
	apenArquivo()
	getToken()
	self.soma()
	consome(tkEOF)
	fechaAqrquivo()

# OK
def soma(self):
	#soma = mult resto soma
	res1 = self.mult()
	res2 = self.restoSoma()
	res = res1 + res2
	return res

# OK
def restoSoma():
	#restosoma = vazio | + mult resto soma | - mult resto soma
	if (Atual.token == tkmais):
		consome(tkmais)
		self.mult()
		self.restoSoma()
	elif (Atual.token == tkmenos):
		#print("ident")
		self.mult()
		self.restoSoma()
	else:
		pass	

# OK
def consome(self):
	if(Token == Atual.token):
		getToken()
	else:
		print("ERRO: era esperado o Token "+msg(Token+", mas veio o Token "+msg(Atual.token)+": linha "+Atual.linha+", coluna: "Atual.coluna+"\n"))

# OK
def fator(self):
	if (Atual.token == Token.ident):
		if (Token.lexema in tabSimb):
			res = tabSimb[Atual.lexema]
		else:
			raise Exception("variavel nao declarada")
		consome(Token.ident)
	elif(Atual.token == Token.abrePar):
		consome(Token.abrePar)
		res = self.soma()
		consome(Token.fechaPar)
	else:
		if (Atual.token == Token.num):
			res == int (Atual.lexema)
		consome(Token.num)
	return res

# OK
def mult(self):
	uno()
	restoMult()

# OK
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

# OK
def uno(self):
	if(Atual.token == tkMais):
		consome(tkMais)
		uno()
	elif(Atual.token == tkMenos):
		consome(tkMenos)
		uno()
	else
		fator()
	
def entra():
	consome(Token.input)
	consome(Token.abrePar)
	if (Atual.token == Token.strg):
		print(Token.lexema)
	consome(Token.strg)
	consome(Token.virg)
	if(Atual.token == Token.ident):
		res = input()
		tabSimb[Atual.lexema] = float(res)
		consome(Token.ident)
		consome(Token.fechaPar)
		consome(Token.ptoVirg)
