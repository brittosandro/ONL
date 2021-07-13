from extrai_dados_ONL import ExtraiDados as ed
from calcula_processos_ONL import CalculaProcessosONL as cpONL


class CriaTabela:

    def __init__(self, *valores):
        self.cria_tabela(valores)

    def cria_tabela(self, valores):
        #nome_tabela = input('Informe o nome da Tabela: ')
        nome_tabela = valores[0].replace('ONL_', '').replace('log', 'dat')
        arq = open(nome_tabela, 'w')

        arq.write('  ############################################################\n')
        arq.write('  #                                                          #\n')
        arq.write('  #            Dados de Processos ONL                        #\n')
        arq.write('  #                                                          #\n')
        arq.write('  ############################################################\n\n\n')

        arq.write('{} {:>55}\n'.format('Processo', 'Polarizabilidade Média <alfa> 10**-24 esu'))
        arq.write('-' * 70 + '\n')
        arq.write('{:>5} {:26.7f}\n'.format('Alfa(0;0)', float(valores[1])))
        arq.write('-' * 70 + '\n')
        arq.write('{:>5} {:25.7f}\n'.format('Alfa(-w;w)', float(valores[2])))
        arq.write('-' * 70 + '\n\n')

        arq.write('{} {:>47}\n'.format('Processo', 'Primeira Hiper  Total 10**-30 esu'))
        arq.write('-' * 70 + '\n')
        arq.write('{:>5} {:25.7f}\n'.format('Beta(0;0,0)', float(valores[3])))
        arq.write('-' * 70 + '\n')
        arq.write('{:>5} {:25.7f}\n'.format('Beta(-2w;w,w)', float(valores[7])))
        arq.write('-' * 70 + '\n\n')

        arq.write('{} {:>47}\n'.format('Processo', 'Primeira Hiper  b_vec 10**-30 esu'))
        arq.write('-' * 70 + '\n')
        arq.write('{:>5} {:25.7f}\n'.format('Beta(0;0,0)', float(valores[4])))
        arq.write('-' * 70 + '\n')
        arq.write('{:>5} {:25.7f}\n'.format('Beta(-2w;w,w)', float(valores[8])))
        arq.write('-' * 70 + '\n\n')

        arq.write('{} {:>52}\n'.format('Processo', 'Primeira Hiper  mi_beta_vec 10**-48 esu'))
        arq.write('-' * 70 + '\n')
        arq.write('{:>5} {:25.7f}\n'.format('Beta(0;0,0)', float(valores[5])))
        arq.write('-' * 70 + '\n')
        arq.write('{:>5} {:25.7f}\n'.format('Beta(-2w;w,w)', float(valores[9])))
        arq.write('-' * 70 + '\n\n')

        arq.write('{} {:>59}\n'.format('Processo', 'Primeira Hiper  beta_vec_T_||_(z) 10**-30 esu'))
        arq.write('-' * 70 + '\n')
        arq.write('{:>5} {:25.7f}\n'.format('Beta(0;0,0)', float(valores[6])))
        arq.write('-' * 70 + '\n')
        arq.write('{:>5} {:25.7f}\n'.format('Beta(-2w;w,w)', float(valores[10])))
        arq.write('-' * 70 + '\n\n')

        arq.write('{} {:>51}\n'.format('Processo', 'Segunda Hiper  gama_medio 10**-36 esu'))
        arq.write('-' * 70 + '\n')
        arq.write('{:>5} {:25.7f}\n'.format('gama(0;0,0,0)', float(valores[11])))
        arq.write('-' * 70 + '\n')
        arq.write('{:>5} {:25.7f}\n'.format('gama(-w;w,0,0)', float(valores[12])))
        arq.write('-' * 70 + '\n')
        arq.write('{:>5} {:25.7f}\n'.format('gama(-2w;w,w,0)', float(valores[13])))
        arq.write('-' * 70 + '\n\n')

        arq.write('{} {:>51}\n'.format('Processo', 'Segunda Hiper  Z SCAN 10**-36 esu'))
        arq.write('-' * 70 + '\n')
        arq.write('{:>5} {:25.7f}\n'.format('gama(-w;w,0,0)', float(valores[14])))
        arq.write('-' * 70 + '\n\n')

        #arq.write('{} {:>43}\n'.format('Const. Dieletrica', 'Alfa estatico 10**-40 C**2 m**2 J**-1'))
        #arq.write('-' * 70 + '\n')
        #arq.write('{:>5} {:25.7f}\n'.format('EPSILON', float(valores[16])))
        #arq.write('-' * 70 + '\n')

        arq.close()

class CriaTabelaDadosONL:

    ''' Essa classe Extrai e processa dados ONL dos arquivos *.log
    para criar Tabelas com os dados de interesse. '''

    def __init__(self, lista_dados):
        self.lista_dados = lista_dados
        self.cria_tabela()

    def cria_tabela(self):
        for arq in self.lista_dados:
            if arq.endswith('.log'):
                ## Relação de dados momento de dipolo
                dados_de_dipolo = ed(arq).extrai_momento_dipolo()
                componentes_mom_dip = cpONL(dados_de_dipolo)

                ## Relação de dados alfa(0;0)
                alfa_proc_00 = ed(arq).extrai_polariz_alfa_00()
                valor_alfa_00 = cpONL(alfa_proc_00).calc_polarizabilidade_media()

                ## Relação de dados alfa(w;w)
                alfa_proc_ww = ed(arq).extrai_polariz_alfa_ww()
                valor_alfa_ww = cpONL(alfa_proc_ww).calc_polarizabilidade_media()

                ## Relação de dados e calculos beta(0;0,0)
                dados_beta_000 = ed(arq).extrai_beta_000()
                componentes_beta_000 = cpONL(dados_beta_000)

                beta_tot_000 = cpONL.calc_beta_tot(componentes_beta_000)
                beta_vec_000 = cpONL.calc_beta_vec(componentes_beta_000, componentes_mom_dip)
                mi_beta_000 = cpONL.calc_mi_beta(componentes_beta_000, componentes_mom_dip)
                beta_z_T_000 = cpONL.calc_beta_vec_T_Z(componentes_beta_000)

                ## Relação de dados beta(-2w;w,w)
                dados_beta_2www = ed(arq).extrai_beta_2www()
                componentes_beta_2www = cpONL(dados_beta_2www)

                beta_tot_2www = cpONL.calc_beta_tot(componentes_beta_2www)
                beta_vec_2www = cpONL.calc_beta_vec(componentes_beta_2www, componentes_mom_dip)
                mi_beta_2www = cpONL.calc_mi_beta(componentes_beta_2www, componentes_mom_dip)
                beta_z_T_2www = cpONL.calc_beta_vec_T_Z(componentes_beta_2www)

                ## Relação de dados gama(0;0,0,0)
                dados_gama_0000 = ed(arq).extrai_gama_0000()
                gama_medio_0000 = cpONL(dados_gama_0000).gama_medio()

                ## Relação de dados Gama(-w;w,0,0)
                dados_gama_ww00 = ed(arq).extrai_gama_ww00()
                gama_medio_ww00 = cpONL(dados_gama_ww00).gama_medio()

                ##Relação para se calcular gamma z scan
                gama_z_scan = cpONL.calc_gama_z_scan(gama_medio_0000, gama_medio_ww00)

                ## Relação de dados gama(-2w;w,w,0)
                dados_gama_2www0 = ed(arq).extrai_gama_2www0()
                gama_medio_2www0 = cpONL(dados_gama_2www0).gama_medio()

                ## Dados alfa(0;0) para calcular constante dieletrica
                #if i == 2:
                    #alfa_dados_dieletric = ed(sys.argv[i]).extrai_polariz_alfa_00_para_const_dieletric()
                    #valor_constante_dieletric = cpONL(alfa_dados_dieletric).calc_const_dieletrica()
                #else:
                    #valor_constante_dieletric = 0

                CriaTabela(arq, valor_alfa_00, valor_alfa_ww,
                       beta_tot_000, beta_vec_000, mi_beta_000, beta_z_T_000,
                       beta_tot_2www, beta_vec_2www, mi_beta_2www, beta_z_T_2www,
                       gama_medio_0000, gama_medio_ww00, gama_medio_2www0, gama_z_scan)


if __name__ == '__main__':
    import os

    caminho = os.getcwd() + '/'
    lista_dados = os.listdir(caminho)
    TrabalhaDadosONL(lista_dados)
