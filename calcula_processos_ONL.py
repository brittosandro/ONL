import numpy as np


class CalculaProcessosONL:

    def __init__(self, dados_brutos):
        self.dados = dados_brutos

    def comps_momento_dipolo(self):
        if type(self.dados) == type(dict()):
            val_comps_mom_dip = []
            for comp, val in zip(self.dados.keys(), self.dados.values()):
                if comp in ('x', 'y', 'z'):
                    val_comps_mom_dip.append(val)
                    #valores_comps_mom_dip.append(float(val)**2)
            return val_comps_mom_dip
        else:
            valores_comps_mom_dip = []
            for i in range(len(self.dados)):
                valores_parc = []
                for comp, val in zip(self.dados[i].keys(), self.dados[i].values()):
                    if comp == 'Tot':
                        continue
                    else:
                        valores_parc.append(float(val))
                    #print(valores_parc)
                valores_comps_mom_dip.append(sum(valores_parc))
            #print(valores_comps_mom_dip)
            return valores_comps_mom_dip

    def calc_polarizabilidade_media(self):
        if type(self.dados) == type(dict()):
            lista_val = []
            for comp, val in zip(self.dados.keys(), self.dados.values()):
                if comp in ('xx', 'yy', 'zz'):
                    lista_val.append(float(val))
            polarizabilidade_media = sum(lista_val) / 3
            return polarizabilidade_media

    def pega_comps_beta_xyz(self):
        if type(self.dados) == type(dict()):
            vals_comps_xyz  = []
            for comp, val in zip(self.dados.keys(), self.dados.values()):
                if comp in ('x', 'y', 'z'):
                    vals_comps_xyz.append(val)
        return vals_comps_xyz

    #def comps_beta_2www_xyz(self):
    #    if type(self.dados) == type(dict()):
    #        val_comp_beta_xyz = []
    #        for comp, val in zip(self.dados.keys(), self.dados.values()):
    #            if  comp in ('x', 'y', 'z'):
    #                val_comp_beta_xyz.append(val)
    #    return val_comp_beta_xyz

    def pega_comps_beta_paralelo(self):

        '''
        Esse método armazena o valor da componente de beta dependente da
        frequência, no processo(-2w,w,w) a componente em questão é beta_||_(z).
        '''

        val_comps = []
        for comp, val in zip(self.dados.keys(), self.dados.values()):
           if comp == '|| (z)':
              val_comps.append(val)
              break
        return val_comps

    def gama_medio(self):

        '''
        Esse método extrai o primeiro valor do dicionário, cuja componente é ||
        Nosso interesse é somente pelo gama médio.
        '''

        val_comps = []
        for comp, val in zip(self.dados.keys(), self.dados.values()):
           if comp == '||':
              val_comps.append(val)
              break
        return val_comps[0]

    @classmethod
    def calc_beta_tot(self, dados_comps):
        return np.sqrt(sum(float(valor)**2 for valor in dados_comps.pega_comps_beta_xyz()))

    @classmethod
    def calc_beta_vec(self, comps_beta, comps_mom):
        mult_parc = []
        for comp_dip, comp_beta in zip(comps_mom.comps_momento_dipolo(), comps_beta.pega_comps_beta_xyz()):
            mult_parc.append(float(comp_dip) * float(comp_beta))

        mi_total = np.sqrt(sum([float(valor_comp)**2 for valor_comp in comps_mom.comps_momento_dipolo()]))

        beta_vec = sum(mult_parc) / mi_total
        return beta_vec

    @classmethod
    def calc_mi_beta(self, comps_beta, comps_mom):
        mult_termos = []
        for comp_dip, comp_beta_2www in zip(comps_mom.comps_momento_dipolo(), comps_beta.pega_comps_beta_xyz()):
            mult_termos.append(float(comp_dip) * float(comp_beta_2www))

        mi_b = sum(mult_termos)
        return mi_b

    @classmethod
    def calc_beta_vec_T_Z(self, vals_beta):
        valor_beta_paralelo = vals_beta.pega_comps_beta_paralelo()[0]
        return (5/3) * float(valor_beta_paralelo)

    @classmethod
    def calc_gama_z_scan(self, gama0000, gamaww00):

       #  Esse método cálcula a equação: 2*gamma(-w;w,0,0) - gamma(0;0,0,0)
       #  Representa o Gama medido experimentalmente viz z scan

       return 2*float(gamaww00) - float(gama0000)


    def calc_const_dieletrica(self):

        ''' Esse metodo calcula a constante dieletrica para molecula de
        interesse usando a equacao de Claussius-Mossoti.'''

        epsilon_0 = 8.854*10**(-12)
        volume = float(input('Informe o Volume do Cristal: '))
        numero_moleculas = 4
        N = (numero_moleculas / volume)*(1 / 10**(-30))
        alfa = float(self.dados[1])*(10**(-40))
        k = (N*alfa) / epsilon_0
        epsilon = (2*k + 3) / (3 - k)

        return epsilon




if __name__ == '__main__':

    #testa = CalculaProcessosONL({'|| (z)': '-0.980179e+02', '_|_(z)': '-0.326726e+02', 'x': '-0.824693e+03', 'y': '0.278137e+03', 'z': '-0.490090e+03', '||': '0.199766e+03', 'xxx': '-0.187088e+03', 'xxy': '0.659958e+02', 'yxy': '-0.216630e+02', 'yyy'
    #: '0.592700e+01', 'xxz': '-0.112932e+03', 'yxz': '0.381170e+02', 'yyz': '-0.125684e+02', 'zxz': '-0.661468e+02', 'zyz': '0.207894e+02', 'zzz': '-0.378625e+02'})

    #testa1 = CalculaProcessosONL({'Tot': '0.238784e+02', 'x': '-0.197838e+02', 'y': '0.668087e+01', 'z': '-0.115820e+02'})

    e = CalculaProcessosONL(('iso', '0.639346e+02')).calc_const_dieletrica()
    print(e)


    '''
    print('beta_tot(0;0,0) =  ', CalculaProcessosONL.calc_beta_tot(testa))
    print('beta_vec(0;0,0) = ', CalculaProcessosONL.calc_beta_vec(testa, testa1))
    print('mi beta_vec(0;0,0) = ', CalculaProcessosONL.calc_mi_beta(testa, testa1))
    print('beta_z_T(0;0,0) = ', CalculaProcessosONL.calc_beta_vec_T_Z(testa))
    print('-' * 70)

    testa2 = CalculaProcessosONL({'|| (z)': '-0.448852e+03', '_|_(z)': '-0.149211e+03', 'x': '-0.379381e+04',
    'y': '0.128840e+04', 'z': '-0.224426e+04', '||': '0.918470e+03', 'xxx': '-0.862900e+03', 'yxx': '0.295091e+03',
    'zxx': '-0.512170e+03', 'xyx': '0.297072e+03', 'yyx': '-0.998691e+02', 'zyx': '0.174494e+03',
    'xyy': '-0.991805e+02', 'yyy': '0.320703e+02', 'zyy': '-0.583086e+02', 'xzx': '-0.512933e+03',
    'yzx': '0.173599e+03', 'zzx': '-0.302245e+03', 'xzy': '0.174612e+03', 'yzy': '-0.587638e+02',
    'zzy': '0.101243e+03', 'xzz': '-0.301699e+03', 'yzz': '0.100471e+03', 'zzz': '-0.176796e+03'})

    print('beta_tot(-2w;w,w) = ', CalculaProcessosONL.calc_beta_tot(testa2))
    print('beta_vec(-2w;w,w) = ', CalculaProcessosONL.calc_beta_vec(testa2, testa1))
    print('mi beta_vec(-2w;w,w) = ', CalculaProcessosONL.calc_mi_beta(testa2, testa1))
    print('beta_z_T(-2w;w,w) = ', CalculaProcessosONL.calc_beta_vec_T_Z(testa2))
    print('-' * 70)

    testa3 = CalculaProcessosONL({'||': '0.113073e+04', '_|_': '0.376909e+03', 'xxxx': '0.257813e+04',
    'xxyx': '-0.860903e+03', 'xxyy': '0.306456e+03', 'yxyy': '-0.105326e+03', 'yyyy': '0.777007e+02',
    'xxzx': '0.148879e+04', 'xxzy': '-0.507748e+03', 'yxzy': '0.175506e+03', 'yyzy': '-0.510455e+02',
    'xxzz': '0.890124e+03', 'yxzz': '-0.307778e+03', 'yyzz': '0.125502e+03', 'zxzz': '0.525363e+03',
    'zyzz': '-0.174123e+03', 'zzzz': '0.354915e+03'})

    print('Gama_medio(0;0,0,0) = ', testa3.gama_medio())
    '''
