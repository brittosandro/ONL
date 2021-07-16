from cria_diretorio import CriaDiretorio
from move_arquivos import MoveArquivos
from cria_graficos import CriaGraficos
import os
import re

class MudaDiretorio:

    def __init__(self, PATH):
        lista_dados = os.listdir(PATH)

        #print(lista_dados)
        #print(PATH)
        dic_todos_processos = {}
        dic_alfa_estatico = {}
        dic_alfa_dinamico = {}
        dic_beta_estatico = {}
        dic_beta_dinamico = {}
        dic_beta_vec_estatico = {}
        dic_beta_vec_dinamico = {}
        dic_mi_beta_vec_estatico = {}
        dic_mi_beta_vec_dinamico = {}
        dic_beta_vec_T_paralelo_estatico = {}
        dic_beta_vec_T_paralelo_dinamico = {}
        dic_gama_estatico = {}
        dic_gama_dinamico = {}
        dic_gama_dinamico_Z_SCAN = {}
        dic_gama_dinamico_2www0 = {}

        for arquivo in lista_dados:
            metodo = re.sub(r'\w+_', r'', arquivo).replace('.dat', '')
            with open(PATH+arquivo) as f:
               arq = f.read()

            padrao_alfa_estatico = re.compile(r'(Alfa\(0;0\))([ ]+)([ |-]\d+.\d+)')
            padrao_alfa_dinamico = re.compile(r'(Alfa\(-w;w\))([ ]+)([ |-]\d+.\d+)')
            padrao_beta_estatico = re.compile(r'(Beta\(0;0,0\))([ ]+)([ |-]\d+.\d+)')
            padrao_beta_dinamico = re.compile(r'(Beta\(-2w;w,w\))([ ]+)([ |-]\d+.\d+)')
            padrao_gama_estatico = re.compile(r'(gama\(0;0,0,0\))([ ]+)([ |-]\d+.\d+)')
            padrao_gama_dinamico_ww00 = re.compile(r'(gama\(-w;w,0,0\))([ ]+)([ |-]\d+.\d+)')
            padrao_gama_dinamico_2www0 = re.compile(r'(gama\(-2w;w,w,0\))([ ]+)([ |-]\d+.\d+)')

            #print(padrao_gama_dinamico_2www0.findall(arq))

            if padrao_alfa_estatico.findall(arq)[0][0]:
               #print(padrao_alfa_estatico.findall(arq)[0][0])
               valor_alfa_estatico = padrao_alfa_estatico.findall(arq)[0][2]
               dic_alfa_estatico[metodo] = float(valor_alfa_estatico)
               dic_todos_processos[padrao_alfa_estatico.findall(arq)[0][0]] = dic_alfa_estatico

            if padrao_alfa_dinamico.findall(arq)[0][0]:
               valor_alfa_dinamico = padrao_alfa_dinamico.findall(arq)[0][2]
               dic_alfa_dinamico[metodo] = float(valor_alfa_dinamico)
               dic_todos_processos[padrao_alfa_dinamico.findall(arq)[0][0]] = dic_alfa_dinamico

            if padrao_beta_estatico.findall(arq)[0][0]: #pega o beta total estatico
               valor_beta_estatico = padrao_beta_estatico.findall(arq)[0][2]
               dic_beta_estatico[metodo] = float(valor_beta_estatico)
               dic_todos_processos[padrao_beta_estatico.findall(arq)[0][0]] = dic_beta_estatico

            if padrao_beta_dinamico.findall(arq)[0][0]: #pega o beta total dinamico
               valor_beta_dinamico = padrao_beta_dinamico.findall(arq)[0][2]
               dic_beta_dinamico[metodo] = float(valor_beta_dinamico)
               dic_todos_processos[padrao_beta_dinamico.findall(arq)[0][0]] = dic_beta_dinamico

            if padrao_beta_estatico.findall(arq)[1]: #pega o beta vec estatico
               #print(padrao_beta_estatico.findall(arq)[1][0])
               valor_beta_vec_estatico = padrao_beta_estatico.findall(arq)[1][2]
               dic_beta_vec_estatico[metodo] = float(valor_beta_vec_estatico)
               nome_beta_vec_estatico = padrao_beta_estatico.findall(arq)[1][0] + '_VEC_ESTATICO'
               dic_todos_processos[nome_beta_vec_estatico] = dic_beta_vec_estatico

            if padrao_beta_dinamico.findall(arq)[1]: #pega o beta vec dinamico
               valor_beta_vec_dinamico = padrao_beta_dinamico.findall(arq)[1][2]
               dic_beta_vec_dinamico[metodo] = float(valor_beta_vec_dinamico)
               nome_beta_vec_dinamico = padrao_beta_dinamico.findall(arq)[1][0] + '_VEC_DINAMICO'
               dic_todos_processos[nome_beta_vec_dinamico] = dic_beta_vec_dinamico

            if padrao_beta_estatico.findall(arq)[2]: #pega mibeta vec estatico
               valor_mibeta_vec_estatico = padrao_beta_estatico.findall(arq)[2][2]
               dic_mi_beta_vec_estatico[metodo] = float(valor_mibeta_vec_estatico)
               nome_mi_beta_vec_estatico = padrao_beta_estatico.findall(arq)[2][0] + '_MI_BETA_VEC_EST'
               dic_todos_processos[nome_mi_beta_vec_estatico] = dic_mi_beta_vec_estatico

            if padrao_beta_dinamico.findall(arq)[2]: #pega mibeta vec dinamico
               valor_mibeta_vec_dinamico = padrao_beta_dinamico.findall(arq)[2][2]
               dic_mi_beta_vec_dinamico[metodo] = float(valor_mibeta_vec_dinamico)
               nome_mi_beta_vec_dinamico = padrao_beta_dinamico.findall(arq)[2][0] + '_MI_BETA_VEC_DIN'
               dic_todos_processos[nome_mi_beta_vec_dinamico] = dic_mi_beta_vec_dinamico

            if padrao_beta_estatico.findall(arq)[3]: #pega beta vec || estático
               valor_beta_T_estatico =  padrao_beta_estatico.findall(arq)[3][2]
               dic_beta_vec_T_paralelo_estatico[metodo] = float(valor_beta_T_estatico)
               nome_beta_vec_T_estatico = padrao_beta_estatico.findall(arq)[3][0] + '_BETA_VEC_T_EST'
               dic_todos_processos[nome_beta_vec_T_estatico] = dic_beta_vec_T_paralelo_estatico

            if padrao_beta_dinamico.findall(arq)[3]: #pega beta vec ||  dinâmico
               valor_beta_T_dinamico =  padrao_beta_dinamico.findall(arq)[3][2]
               dic_beta_vec_T_paralelo_dinamico[metodo] = float(valor_beta_T_dinamico)
               nome_beta_vec_T_dinamico = padrao_beta_dinamico.findall(arq)[3][0] + '_BETA_VEC_T_DIN'
               dic_todos_processos[nome_beta_vec_T_dinamico] = dic_beta_vec_T_paralelo_dinamico


            if padrao_gama_estatico.findall(arq)[0]: #pega gama estatico
               valor_gama_estatico = padrao_gama_estatico.findall(arq)[0][2]
               dic_gama_estatico[metodo] = float(valor_gama_estatico)
               nome_gama_estatico = padrao_gama_estatico.findall(arq)[0][0] + '_ESTATICO'
               dic_todos_processos[nome_gama_estatico] = dic_gama_estatico

            if padrao_gama_dinamico_ww00.findall(arq)[0]: #pega gama médio dinâmico (-w,w,0,0)
               valor_gama_dinamico_ww00 = padrao_gama_dinamico_ww00.findall(arq)[0][2]
               dic_gama_dinamico[metodo] = float(valor_gama_dinamico_ww00)
               nome_gama_dinamico_ww00 = padrao_gama_dinamico_ww00.findall(arq)[0][0] + '_ww00'
               dic_todos_processos[nome_gama_dinamico_ww00] = dic_gama_dinamico

            if padrao_gama_dinamico_2www0.findall(arq)[0]: #pega gama médio dinâmico (-2w, w, w, 0)
               valor_gama_dinamico_2www0 = padrao_gama_dinamico_2www0.findall(arq)[0][2]
               dic_gama_dinamico_2www0[metodo] = float(valor_gama_dinamico_2www0)
               nome_gama_dinamico_2www0 = padrao_gama_dinamico_2www0.findall(arq)[0][0]
               dic_todos_processos[nome_gama_dinamico_2www0] = dic_gama_dinamico_2www0

            if padrao_gama_dinamico_ww00.findall(arq)[0]: #pega gama Z-SCAN dinâmico (-w,w,0,0)
               valor_gama_dinamico_Z_SCAN = padrao_gama_dinamico_ww00.findall(arq)[1][2]
               dic_gama_dinamico_Z_SCAN[metodo] = float(valor_gama_dinamico_Z_SCAN)
               nome_gama_Z_SCAN_dinamico_ww00 = padrao_gama_dinamico_ww00.findall(arq)[0][0] + '_Z_SCAN_ww00'
               dic_todos_processos[nome_gama_Z_SCAN_dinamico_ww00] = dic_gama_dinamico_Z_SCAN



        '''
        print(dic_todos_processos)
        print(dic_alfa_estatico)
        print(dic_alfa_dinamico)
        print(dic_beta_estatico)
        print(dic_beta_dinamico)
        print(dic_beta_vec_estatico)
        print(dic_beta_vec_dinamico)
        print(dic_mi_beta_vec_estatico)
        print(dic_mi_beta_vec_dinamico)
        print(dic_beta_vec_T_paralelo_estatico)
        print(dic_beta_vec_T_paralelo_dinamico)
        print(dic_gama_estatico)
        print(dic_gama_dinamico)
        print(dic_gama_dinamico_Z_SCAN)
        print(dic_gama_dinamico_2www0)
        '''

        for processo in dic_todos_processos.keys():
            if processo == 'Alfa(0;0)':
                nome_arquivo = 'alfa_estatico.txt'
                with open(PATH+nome_arquivo, 'w') as f:
                    for metodo, valor in sorted(dic_alfa_estatico.items()):
                        f.write('{:<12} {:<27}\n'.format(metodo, round(valor, 5)))
                novo_diretorio = nome_arquivo.replace('.txt', '') + '/'
                CriaDiretorio(PATH, novo_diretorio)
                MoveArquivos(PATH, novo_diretorio, nome_arquivo)
                CriaGraficos(PATH, novo_diretorio+nome_arquivo)

            if processo == 'Alfa(-w;w)':
                nome_arquivo = 'alfa_dinamico.txt'
                with open(PATH+nome_arquivo, 'w') as f:
                    for metodo, valor in sorted(dic_alfa_dinamico.items()):
                        f.write('{:<12} {:<27}\n'.format(metodo, round(valor, 5)))
                novo_diretorio = nome_arquivo.replace('.txt', '') + '/'
                CriaDiretorio(PATH, novo_diretorio)
                MoveArquivos(PATH, novo_diretorio, nome_arquivo)
                CriaGraficos(PATH, novo_diretorio+nome_arquivo)

            if processo == 'Beta(0;0,0)':
                nome_arquivo = padrao_beta_estatico.findall(arq)[0][0] + '_beta_estatico_total.txt'
                with open(PATH+nome_arquivo, 'w') as f:
                    for metodo, valor in sorted(dic_beta_estatico.items()):
                        f.write('{:<12} {:<27}\n'.format(metodo, round(valor, 5)))
                novo_diretorio = nome_arquivo.replace('.txt', '') + '/'
                CriaDiretorio(PATH, novo_diretorio)
                MoveArquivos(PATH, novo_diretorio, nome_arquivo)

            if processo == 'Beta(-2w;w,w)':
                nome_arquivo = padrao_beta_dinamico.findall(arq)[0][0] + '_beta_dinamico.txt'
                with open(PATH+nome_arquivo, 'w') as f:
                    for metodo, valor in sorted(dic_beta_dinamico.items()):
                        f.write('{:<12} {:<27}\n'.format(metodo, round(valor, 5)))
                novo_diretorio = nome_arquivo.replace('.txt', '') + '/'
                CriaDiretorio(PATH, novo_diretorio)
                MoveArquivos(PATH, novo_diretorio, nome_arquivo)
                CriaGraficos(PATH, novo_diretorio+nome_arquivo)

            if processo == 'Beta(0;0,0)_VEC_ESTATICO':
                nome_arquivo =  'Beta(0;0,0)_VEC_ESTATICO.txt'
                with open(PATH+nome_arquivo, 'w') as f:
                    for metodo, valor in sorted(dic_beta_vec_estatico.items()):
                        f.write('{:<12} {:<27}\n'.format(metodo, round(valor, 5)))
                novo_diretorio = nome_arquivo.replace('.txt', '') + '/'
                CriaDiretorio(PATH, novo_diretorio)
                MoveArquivos(PATH, novo_diretorio, nome_arquivo)
                CriaGraficos(PATH, novo_diretorio+nome_arquivo)

            if processo == 'Beta(-2w;w,w)_VEC_DINAMICO':
                nome_arquivo = 'Beta(-2w;w,w)_VEC_DINAMICO.txt'
                with open(PATH+nome_arquivo, 'w') as f:
                    for metodo, valor in sorted(dic_beta_vec_dinamico.items()):
                        f.write('{:<12} {:<27}\n'.format(metodo, round(valor, 5)))
                novo_diretorio = nome_arquivo.replace('.txt', '') + '/'
                CriaDiretorio(PATH, novo_diretorio)
                MoveArquivos(PATH, novo_diretorio, nome_arquivo)

            if processo == 'Beta(0;0,0)_MI_BETA_VEC_EST':
                nome_arquivo = 'Beta(0;0,0)_MI_BETA_VEC_EST.txt'
                with open(PATH+nome_arquivo, 'w') as f:
                    for metodo, valor in sorted(dic_mi_beta_vec_estatico.items()):
                        f.write('{:<12} {:<27}\n'.format(metodo, round(valor, 5)))
                novo_diretorio = nome_arquivo.replace('.txt', '') + '/'
                CriaDiretorio(PATH, novo_diretorio)
                MoveArquivos(PATH, novo_diretorio, nome_arquivo)
                CriaGraficos(PATH, novo_diretorio+nome_arquivo)

            if processo == 'Beta(-2w;w,w)_MI_BETA_VEC_DIN':
                nome_arquivo = 'Beta(-2w;w,w)_MI_BETA_VEC_DIN.txt'
                with open(PATH+nome_arquivo, 'w') as f:
                    for metodo, valor in sorted(dic_mi_beta_vec_dinamico.items()):
                        f.write('{:<12} {:<27}\n'.format(metodo, round(valor, 5)))
                novo_diretorio = nome_arquivo.replace('.txt', '') + '/'
                CriaDiretorio(PATH, novo_diretorio)
                MoveArquivos(PATH, novo_diretorio, nome_arquivo)
                CriaGraficos(PATH, novo_diretorio+nome_arquivo)

            if processo == 'Beta(0;0,0)_BETA_VEC_T_EST':
                nome_arquivo = 'Beta(0;0,0)_BETA_VEC_T_||_EST.txt'
                with open(PATH+nome_arquivo, 'w') as f:
                    for metodo, valor in sorted(dic_beta_vec_T_paralelo_estatico.items()):
                        f.write('{:<12} {:<27}\n'.format(metodo, round(valor, 5)))
                novo_diretorio = nome_arquivo.replace('.txt', '') + '/'
                CriaDiretorio(PATH, novo_diretorio)
                MoveArquivos(PATH, novo_diretorio, nome_arquivo)
                CriaGraficos(PATH, novo_diretorio+nome_arquivo)

            if processo == 'Beta(-2w;w,w)_BETA_VEC_T_DIN':
                nome_arquivo = 'Beta(-2w;w,w)_BETA_VEC_T_||_DIN.txt'
                with open(PATH+nome_arquivo, 'w') as f:
                    for metodo, valor in sorted(dic_beta_vec_T_paralelo_dinamico.items()):
                        f.write('{:<12} {:<27}\n'.format(metodo, round(valor, 5)))
                novo_diretorio = nome_arquivo.replace('.txt', '') + '/'
                CriaDiretorio(PATH, novo_diretorio)
                MoveArquivos(PATH, novo_diretorio, nome_arquivo)
                CriaGraficos(PATH, novo_diretorio+nome_arquivo)

            if processo == 'gama(0;0,0,0)_ESTATICO':
                nome_arquivo = 'gama(0;0,0,0)_ESTATICO.txt'
                with open(PATH+nome_arquivo, 'w') as f:
                    for metodo, valor in sorted(dic_gama_estatico.items()):
                        f.write('{:<12} {:<27}\n'.format(metodo, round(valor, 5)))
                novo_diretorio = nome_arquivo.replace('.txt', '') + '/'
                CriaDiretorio(PATH, novo_diretorio)
                MoveArquivos(PATH, novo_diretorio, nome_arquivo)

            if processo == 'gama(-w;w,0,0)_ww00':
                nome_arquivo = 'gama(-w;w,0,0)_ww00.txt'
                with open(PATH+nome_arquivo, 'w') as f:
                    for metodo, valor in sorted(dic_gama_dinamico.items()):
                        f.write('{:<12} {:<27}\n'.format(metodo, round(valor, 5)))
                novo_diretorio = nome_arquivo.replace('.txt', '') + '/'
                CriaDiretorio(PATH, novo_diretorio)
                MoveArquivos(PATH, novo_diretorio, nome_arquivo)
                CriaGraficos(PATH, novo_diretorio+nome_arquivo)

            if processo == 'gama(-2w;w,w,0)':
                nome_arquivo = 'gama(-2w;w,w,0).txt'
                with open(PATH+nome_arquivo, 'w') as f:
                    for metodo, valor in sorted(dic_gama_dinamico_2www0.items()):
                        f.write('{:<12} {:<27}\n'.format(metodo, round(valor, 5)))
                novo_diretorio = nome_arquivo.replace('.txt', '') + '/'
                CriaDiretorio(PATH, novo_diretorio)
                MoveArquivos(PATH, novo_diretorio, nome_arquivo)
                CriaGraficos(PATH, novo_diretorio+nome_arquivo)


            if processo == 'gama(-w;w,0,0)_Z_SCAN_ww00':
                nome_arquivo = 'gama(-w;w,0,0)_Z_SCAN_ww00.txt'
                with open(PATH+nome_arquivo, 'w') as f:
                    for metodo, valor in sorted(dic_gama_dinamico_Z_SCAN.items()):
                        f.write('{:<12} {:<27}\n'.format(metodo, round(valor, 5)))
                novo_diretorio = nome_arquivo.replace('.txt', '') + '/'
                CriaDiretorio(PATH, novo_diretorio)
                MoveArquivos(PATH, novo_diretorio, nome_arquivo)
                CriaGraficos(PATH, novo_diretorio+nome_arquivo)
                


if __name__ == '__main__':
    caminho = os.getcwd() + '/' + 'Resultados/'
    PATH = os.path.join(caminho)
    #print('-------------------------------------------------------------------')
    #print(PATH)
    MudaDiretorio(PATH)
