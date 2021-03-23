class ExtraiDados:

    def __init__(self, arquivo):
        self.arq = open(arquivo, 'r')
        self.dados_arq = self.arq.read()
        self.arq.close()

        # Gambiarra para funcionar dessa vez
        #self.verifica = int(input('''Deseja Calcular Somente Input Orientation? 1 - sim | 0 - não: '''))
        self.verifica = 1

    def extrai_momento_dipolo(self):

        ''' Esse método extrai os dados de momento de dipolo. Retorna uma
        um dicinário cuja chave é a componente do momento de dipolo e o
        valor é o valor do momento de dipolo em Debye(D).'''

        separador1 = ' Electric dipole moment'
        separador2 = ' Alpha(0;0):'
        comp_mom_de_dipolo = slice(2, 6)
        valor_mom_de_dipolo = slice(30, 44)

        #verifica = int(input('''Deseja Calcular Somente Input Orientation? 1 - sim | 0 - não: '''))

        if self.verifica == 1:
            mom_dipolo_val = {}
            lista_val = self.dados_arq.split(separador1)[1].split(separador2)[0].split('\n')[3:7]
            for dado in lista_val:
                mom_dipolo_val[dado[comp_mom_de_dipolo].strip()] = dado[valor_mom_de_dipolo].strip().replace('D', 'e')
            return mom_dipolo_val
        else:
            ocorrencias = self.dados_arq.count(separador1)
            val_mom_dip = []
            for ocorr in range(1, ocorrencias + 1):
                mom_dipolo_dados = {}
                dados_mom_dip = self.dados_arq.split(separador1)[ocorr].split(separador2)[0].split('\n')[3:7]
                for dado in dados_mom_dip:
                    mom_dipolo_dados[dado[comp_mom_de_dipolo].strip()] = dado[valor_mom_de_dipolo].strip().replace('D', 'e')
                val_mom_dip.append(mom_dipolo_dados)
            return val_mom_dip

    def extrai_polariz_alfa_00(self):

        ''' Esse método extrai os dados estáticos para polarizabilidade, no processo
            alfa(0;0). Retorna um dicionário cuja chave são as componentes dos vetores
            e os valores são as intensidades da polarizabilidade em 10**-30 esu. '''

        separador2 = ' Alpha(0;0):'
        separador3 = ' Alpha(-w;w)'
        comp_alfa_00 = slice(2, 8)
        valor_alfa_00 = slice(31, 44)

        #verifica = int(input('''Deseja Calcular Somente Input Orientation? 1 - sim | 0 - não: '''))

        if self.verifica == 1:
            alfa_00 = {}
            lista_val = self.dados_arq.split(separador2)[1].split(separador3)[0].split('\n')[2:10]
            for dado in lista_val:
                alfa_00[dado[comp_alfa_00].strip()] = dado[valor_alfa_00].strip().replace('D', 'e')
            #print(alfa_00)
            return alfa_00
        else:
            ocorrencias = self.dados_arq.count(separador2)
            alfa_00 = []
            for ocorr in range(1, ocorrencias + 1):
                alfa_00_dados = {}
                dados_alfa_00 = self.dados_arq.split(separador2)[ocorr].split(separador3)[0].split('\n')[2:10]
                for dado in dados_alfa_00:
                    alfa_00_dados[dado[comp_alfa_00].strip()] = dado[valor_alfa_00].strip().replace('D', 'e')
                alfa_00.append(alfa_00_dados)
            #print(val_alfa_00)
            return alfa_00

    def extrai_polariz_alfa_00_para_const_dieletric(self):

        ''' Esse método extrai o valor de polarizabilidade em unidades
        10** -40 SI ou SI units = C**2 m**2 J**-1 para calcularmos a
        constante dielétrica da substancia. Retorna uma tupla com o valor
        da componente isotropica.
        '''

        separador2 = ' Alpha(0;0):'
        separador3 = ' Alpha(-w;w)'

        comp_alfa_00 = slice(2, 8)
        valor_alfa_00 = slice(46, 62)

        if self.verifica == 1:
            lista_val = ''.join(self.dados_arq.split(separador2)[1].split(separador3)[0].split('\n')[2:3])
            dado = (lista_val[comp_alfa_00].strip(), lista_val[valor_alfa_00].strip().replace('D', 'e'))

        return dado

    def extrai_polariz_alfa_ww(self):

        ''' Esse método extrai os dados dinâmicos da polarizabilidade, no processo
            alfa(-w;w) retornando um dicionário cuja chave são as componentes dos
            vetores e os valores são as intensidade da polarizabilidade em  10**-30 esu.  '''

        separador3 = ' Alpha(-w;w)'
        separador4 = ' Beta(0;0,0):'

        comp_alfa_ww = slice(2, 8)
        valor_alfa_ww = slice(31, 44)

        #verifica = int(input('''Deseja Calcular Somente Input Orientation? 1 - sim | 0 - não: '''))

        if self.verifica == 1:
            alfa_ww = {}
            lista_val = self.dados_arq.split(separador3)[1].split(separador4)[0].split('\n')[2:10]
            for dado in lista_val:
                alfa_ww[dado[comp_alfa_ww].strip()] = dado[valor_alfa_ww].strip().replace('D', 'e')
            return alfa_ww

    def extrai_beta_000(self):

        ''' Esse método extrai os dados da primeira hiperpolarizabilidade,
            considerando o caso estático no processo beta(0;0,0). Retorna
            um dicionário cuja chave são as componentes do vetor e os
            valores são as intensidade em 10**-30 esu. '''

        separador4 = ' Beta(0;0,0):'
        separador5 = ' Beta(-w;w,0)'

        comp_beta_000 = slice(2, 9)
        valor_beta_000 = slice(30, 44)



        if self.verifica == 1:
            beta_000 = {}
            lista_dados = self.dados_arq.split(separador4)[1].split(separador5)[0].split('\n')[2:18]
            for dado in lista_dados:
                beta_000[dado[comp_beta_000].strip()] = dado[valor_beta_000].strip().replace('D', 'e')
            return beta_000

    def extrai_beta_2www(self):
        separador6 = ' Beta(-2w;w,w)'
        separador7 = ' Gamma(0;0,0,0):'

        comp_beta_2www = slice(2, 9)
        valor_beta_2www = slice(30, 44)

        if self.verifica == 1:
            valores_beta_2www = {}
            lista0 = self.dados_arq.split(separador6)[1].split(separador7)[0].split('\n')[2:26]
            for comp in lista0:
                valores_beta_2www[comp[comp_beta_2www].strip()] = comp[valor_beta_2www].strip().replace('D', 'e')
        return valores_beta_2www

    def extrai_gama_0000(self):
        separador7 = ' Gamma(0;0,0,0):'
        separador8 = ' Gamma(-w;w,0,0)'

        comp_gama_0000 = slice(2, 7)
        valor_gama_0000 = slice(30, 44)

        if self.verifica == 1:
            valores_gama_0000 = {}
            lista_dados = self.dados_arq.split(separador7)[1].split(separador8)[0].split('\n')[2:19]
            for comp in lista_dados:
                valores_gama_0000[comp[comp_gama_0000].strip()] = comp[valor_gama_0000].strip().replace('D', 'e')
        return valores_gama_0000

    def extrai_gama_ww00(self):
        separador9 = ' Gamma(-w;w,0,0)'
        separador10 = ' Gamma(-2w;w,w,0)'

        comp_gama_ww00 = slice(2, 7)
        valor_gama_ww00 = slice(30, 44)

        if self.verifica == 1:
            valores_gama_ww00 = {}
            lista_dados = self.dados_arq.split(separador9)[1].split(separador10)[0].split('\n')[2:19]
            for comp in lista_dados:
                valores_gama_ww00[comp[comp_gama_ww00].strip()] = comp[valor_gama_ww00].strip().replace('D', 'e')
        return valores_gama_ww00

    def extrai_gama_2www0(self):
        separador10 = ' Gamma(-2w;w,w,0)'
        separador11 = ' ' + '-' * 70

        comp_gama_2www0 = slice(2, 7)
        valor_gama_2www0 = slice(30, 44)

        if self.verifica == 1:
            valores_gama_2www0 = {}
            lista_dados = self.dados_arq.split(separador10)[1].split(separador11)[0].split('\n')[2:26]
            for comp in lista_dados:
                valores_gama_2www0[comp[comp_gama_2www0].strip()] = comp[valor_gama_2www0].strip().replace('D', 'e')
        return valores_gama_2www0


if __name__ == '__main__':

    teste = ExtraiDados('ONL_VSNS_0_B3LYP.log')
    dados_alfa_00 = teste.extrai_polariz_alfa_00()
    print(dados_alfa_00)

    #teste = ExtraiDados("ONL_B0TMC_0_B3LYP.log")
    #verifica = teste.extrai_polariz_alfa_00_para_const_dieletric()
    #print(verifica)


    #mostra = teste.extrai_beta_000()
    #print('Mostra dados beta(0;0,0)')
    #print(mostra)

    #mostra1 = teste.extrai_momento_dipolo()
    #print('Mostra dados Momento dipolo')
    #print(mostra1)

    #mostra2 = teste.extrai_beta_2www()
    #print('Mostra dados beta(-w, w, 0)')
    #print(mostra2)

    #mostra3 = teste.extrai_gama_0000()
    #print('Mostra dados gama(0;0,0,0)')
    #print(mostra3)
