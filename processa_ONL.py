from cria_tabelas import CriaTabelaDadosONL
from cria_diretorio import CriaDiretorio
from move_arquivos import MoveArquivos
#from muda_diretorio import MudaDiretorio
import os


caminho = os.getcwd() + '/'
lista_dados = os.listdir(caminho)
diretorio_corrente = 'Resultados'

CriaDiretorio(diretorio_corrente)
CriaTabelaDadosONL(lista_dados)
MoveArquivos()
#MudaDiretorio(caminho + diretorio_corrente)
