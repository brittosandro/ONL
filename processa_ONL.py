from cria_tabelas import CriaTabelaDadosONL
from cria_diretorio import CriaDiretorio
from move_arquivos import MoveArquivos
from muda_diretorio import MudaDiretorio
import os


diretorio_corrente = os.getcwd() + '/'
arquivos = os.listdir(diretorio_corrente)

# No diretório corrente só há arquivos *.log
CriaTabelaDadosONL(arquivos)

novos_arquivos = os.listdir(diretorio_corrente)
novo_diretorio = 'Resultados/'
CriaDiretorio(diretorio_corrente, novo_diretorio)
MoveArquivos(diretorio_corrente, novo_diretorio, novos_arquivos)
MudaDiretorio(diretorio_corrente + novo_diretorio)
