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
	
	
