import os
import re

class MudaDiretorio:

    def __init__(self, PATH):

        lista_dados = os.listdir(PATH)

        #print(lista_dados)

        conta_processos = 0
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
               valor_alfa_estatico = padrao_alfa_estatico.findall(arq)[0][2]
               dic_alfa_estatico[metodo] = float(valor_alfa_estatico)
            if padrao_alfa_dinamico.findall(arq)[0][0]:
               valor_alfa_dinamico = padrao_alfa_dinamico.findall(arq)[0][2]
               dic_alfa_dinamico[metodo] = float(valor_alfa_dinamico)
            if padrao_beta_estatico.findall(arq)[0][0]: #pega o beta total estatico
               valor_beta_estatico = padrao_beta_estatico.findall(arq)[0][2]
               dic_beta_estatico[metodo] = float(valor_beta_estatico)
            if padrao_beta_dinamico.findall(arq)[0][0]: #pega o beta total dinamico
               valor_beta_dinamico = padrao_beta_dinamico.findall(arq)[0][2]
               dic_beta_dinamico[metodo] = float(valor_beta_dinamico)
            if padrao_beta_estatico.findall(arq)[1]: #pega o beta vec estatico
               valor_beta_estatico = padrao_beta_estatico.findall(arq)[1][2]
               dic_beta_vec_estatico[metodo] = float(valor_beta_estatico)
            if padrao_beta_dinamico.findall(arq)[1]: #pega o beta vec dinamico
               valor_beta_vec_dinamico = padrao_beta_dinamico.findall(arq)[1][2]
               dic_beta_vec_dinamico[metodo] = float(valor_beta_vec_dinamico)
            if padrao_beta_estatico.findall(arq)[2]: #pega mibeta vec estatico
               valor_mibeta_vec_estatico = padrao_beta_estatico.findall(arq)[2][2]
               dic_mi_beta_vec_estatico[metodo] = float(valor_mibeta_vec_estatico)
            if padrao_beta_dinamico.findall(arq)[2]: #pega mibeta vec dinamico
               valor_mibeta_vec_dinamico = padrao_beta_dinamico.findall(arq)[2][2]
               dic_mi_beta_vec_dinamico[metodo] = float(valor_mibeta_vec_dinamico)
            if padrao_beta_estatico.findall(arq)[3]: #pega beta vec || estático
               valor_beta_T_estatico =  padrao_beta_estatico.findall(arq)[3][2]
               dic_beta_vec_T_paralelo_estatico[metodo] = float(valor_beta_T_estatico)
            if padrao_beta_dinamico.findall(arq)[3]: #pega beta vec ||  dinâmico
               valor_beta_T_dinamico =  padrao_beta_dinamico.findall(arq)[3][2]
               dic_beta_vec_T_paralelo_dinamico[metodo] = float(valor_beta_T_dinamico)
            if padrao_gama_estatico.findall(arq)[0]: #pega gama estatico
               valor_gama_estatico = padrao_gama_estatico.findall(arq)[0][2]
               dic_gama_estatico[metodo] = float(valor_gama_estatico)
            if padrao_gama_dinamico_ww00.findall(arq)[0]: #pega gama médio dinâmico (-w,w,0,0)
               valor_gama_dinamico_ww00 = padrao_gama_dinamico_ww00.findall(arq)[0][2]
               dic_gama_dinamico[metodo] = float(valor_gama_dinamico_ww00)
            if padrao_gama_dinamico_2www0.findall(arq)[0]: #pega gama médio dinâmico (-2w, w, w, 0)
               valor_gama_dinamico_2www0 = padrao_gama_dinamico_2www0.findall(arq)[0][2]
               dic_gama_dinamico_2www0[metodo] = float(valor_gama_dinamico_2www0)
            if padrao_gama_dinamico_ww00.findall(arq)[0]: #pega gama Z-SCAN dinâmico (-w,w,0,0)
               valor_gama_dinamico_Z_SCAN = padrao_gama_dinamico_ww00.findall(arq)[1][2]
               dic_gama_dinamico_Z_SCAN[metodo] = float(valor_gama_dinamico_Z_SCAN)

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


if __name__ == '__main__':
    caminho = os.getcwd() + '/' + 'Resultados/'
    PATH = os.path.join(caminho)
    #print('-------------------------------------------------------------------')
    #print(PATH)
    MudaDiretorio(PATH)
