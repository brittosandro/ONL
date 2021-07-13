class MudaDiretorio:

    def __init__(self, PATH):

        lista_dados = os.listdir(PATH)

        print(lista_dados)

        for arquivo in lista_dados:
            with open(PATH+arquivo) as f:
               arq = f.read()
            print(arq)

if __name__ == '__main__':
    import os

    caminho = os.getcwd() + '/' + 'Resultados/'
    PATH = os.path.join(caminho)
    MudaDiretorio(PATH)
