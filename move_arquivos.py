import shutil
import os


class MoveArquivos:

    def __init__(self):
        self.move_arquivos()

    def move_arquivos(self):
        caminho = os.getcwd() + '/'
        lista_dados = os.listdir(caminho)

        for arquivo in lista_dados:
            if arquivo.endswith('.dat'):
                origem = os.path.join(caminho, arquivo)
                destino = os.path.join(caminho+'Resultados/', arquivo)
                #print('Movendo: {} | Para {}'.format(origem, destino))
                shutil.move(origem, destino)


if __name__ == '__main__':
    MoveArquivos()
