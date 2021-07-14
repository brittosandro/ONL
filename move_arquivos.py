import shutil
import os


class MoveArquivos:

    def __init__(self, diretorio_corrente, novo_diretorio, arquivos):
        self.diretorio_corrente = diretorio_corrente
        self.novo_diretorio = novo_diretorio
        self.arquivos = arquivos
        self.move_arquivos()

    def move_arquivos(self):
        #lista_dados = os.listdir(self.diretorio_corrente)

        if type(self.arquivos) is list:
            for arquivo in self.arquivos:
                if arquivo.endswith('.dat'):
                    origem = os.path.join(self.diretorio_corrente, arquivo)
                    #print(f'origen={origem}')
                    destino = os.path.join(self.diretorio_corrente+self.novo_diretorio, arquivo)
                    #print(f'destino={destino}')
                    #print('Movendo: {} | Para {}'.format(origem, destino))
                    shutil.move(origem, destino)
        else:
            if self.arquivos.endswith('.txt'):
                origem = os.path.join(self.diretorio_corrente, self.arquivos)
                #print(f'origen={origem}')
                destino = os.path.join(self.diretorio_corrente+self.novo_diretorio, self.arquivos)
                #print(f'destino={destino}')
                #print('Movendo: {} | Para {}'.format(origem, destino))
                shutil.move(origem, destino)



if __name__ == '__main__':
    MoveArquivos()
