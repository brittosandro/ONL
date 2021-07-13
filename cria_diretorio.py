import os

class CriaDiretorio:

    def __init__(self, nome_diretorio):
        self.nome_diretorio = nome_diretorio

        lista_dados_corrente = os.listdir()

        if self.nome_diretorio not in lista_dados_corrente:
            self.cria_diretorio(self.nome_diretorio)

    
    def cria_diretorio(self, nome_diretorio):
        os.mkdir(nome_diretorio)

if __name__ == '__main__':
    caminho = os.getcwd()+'/'
    print(caminho)
    CriaDiretorio('Resultados')
