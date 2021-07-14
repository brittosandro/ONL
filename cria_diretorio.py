import os

class CriaDiretorio:

    def __init__(self, diretorio_corrente, nome_diretorio):
        self.diretorio_corrente = diretorio_corrente
        self.nome_diretorio = nome_diretorio

        lista_dados_corrente = os.listdir()

        if self.nome_diretorio not in lista_dados_corrente:
            self.cria_diretorio()


    def cria_diretorio(self):
        os.mkdir(self.diretorio_corrente+self.nome_diretorio)

if __name__ == '__main__':
    caminho = os.getcwd()+'/'
    print(caminho)
    CriaDiretorio('Resultados')
