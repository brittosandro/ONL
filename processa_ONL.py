from extrai_dados_ONL import ExtraiDados as ed
from calcula_processos_ONL import CalculaProcessosONL as cpONL
from output_dados import CriaTabela
from cria_muda_diretorio import CriaeMudaDiretorio
import os

caminho = os.getcwd() + '/'
dirs = os.listdir(caminho)
i = 1

for arq in dirs:
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

        CriaTabela(arq, i, valor_alfa_00, valor_alfa_ww,
               beta_tot_000, beta_vec_000, mi_beta_000, beta_z_T_000,
               beta_tot_2www, beta_vec_2www, mi_beta_2www, beta_z_T_2www,
               gama_medio_0000, gama_medio_ww00, gama_medio_2www0, gama_z_scan)

CriaeMudaDiretorio()       
