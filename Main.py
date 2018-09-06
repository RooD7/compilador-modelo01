"""
Modelo 01
	Compilador basico

Tipo de Compilador:
	Top-Down Descendente Recursivo Preditivo
"""
import Lexico
import argparse
import sys

class Main:
	"""docstring for main"""

	file =sys.argv[1]
	print(file)
	arquivo = open(file, 'r')
	lexico = Lexico.Arquivo(arquivo.read())
	Token = lexico.getToken()
	print('Token: ',Token)

