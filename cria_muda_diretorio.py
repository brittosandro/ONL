import shutil
import os


class CriaeMudaDiretorio:

    def __init__(self):
        self.cria_diretorio()
        self.muda_arquivos_de_diretorio()

    def cria_diretorio(self):
        os.mkdir('resultados')

    def muda_arquivos_de_diretorio(self):
        caminho = os.getcwd() + '/'
        dirs = os.listdir(caminho)

        for file in dirs:
            if file.endswith('.dat'):
                origem = os.path.join(caminho, file)
                destino = os.path.join(caminho+'resultados/', file)
                #print('Movendo: {} | Para {}'.format(origem, destino))
                shutil.move(origem, destino)
