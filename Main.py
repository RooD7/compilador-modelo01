import Lexico
import argparse
import sys

class Main:
	"""docstring for main"""

	file =sys.argv[1]
	print(file)
	arquivo = open(file, 'r')
	lexico = Lexico.Arquivo(arquivo.read())
	token = lexico.getToken()
	print('Token: ',token)

