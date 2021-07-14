from cria_tabelas import CriaTabelaDadosONL
from cria_diretorio import CriaDiretorio
from move_arquivos import MoveArquivos
import time
#from muda_diretorio import MudaDiretorio
import os


diretorio_corrente = os.getcwd() + '/'
arquivos = os.listdir(diretorio_corrente)
CriaTabelaDadosONL(arquivos)

novos_arquivos = os.listdir(diretorio_corrente)

nome_novo_diretorio = 'Resultados'
CriaDiretorio(diretorio_corrente, nome_novo_diretorio)

MoveArquivos(diretorio_corrente, nome_novo_diretorio, novos_arquivos)
#MudaDiretorio(caminho + diretorio_corrente)
