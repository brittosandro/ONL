import numpy as np


def valores_polarizabilidade():
    valores1 = np.loadtxt('alfa(0;0)_input_ori_0.dat', skiprows=2, usecols=[1])
    valores2 = np.loadtxt('alfa(-w,w)_input_ori_0.dat', skiprows=2, usecols=[1])
    dados_interesse1 = [valores1[i] for i in (0, 2, 5)]
    dados_interesse2 = [valores2[i] for i in (0, 2, 5)]
    return dados_interesse1, dados_interesse2


def polarizabilidade_media():
    valores1, valores2 = valores_polarizabilidade()
    pol_media1 = sum(valores1)/3
    pol_media2 = sum(valores2)/3
    return pol_media1, pol_media2

def valores_primeira_hiper():
    valores = np.loadtxt('beta(0;0,0)_input_ori_0.dat', skiprows=6, usecols=[1])
    beta_x = [valores[i] for i in (0, 2, 7)]
    beta_y = [valores[i] for i in (1, 3, 8)]
    beta_z = [valores[i] for i in (4, 6, 9)]
    beta_000 = (beta_x, beta_y, beta_z)

    valores_ww = np.loadtxt('beta(-w;w,0)_input_ori_0.dat', skiprows=6, usecols=[1])
    beta_x_ww = [valores_ww[i] for i in (0, 2, 7)]
    beta_y_ww = [valores_ww[i] for i in (1, 3, 8)]
    beta_z_ww = [valores_ww[i] for i in (4, 6, 9)]
    beta_ww0 = (beta_x_ww, beta_y_ww, beta_z_ww)

    lista_de_betas = [beta_000, beta_ww0, ]
    return lista_de_betas


def calcula_beta_vec(valores_beta):
    quadrado_beta = [np.square(sum(betas)) for betas in valores_primeira_hiper()[0]]
    beta_vec_000 = np.sqrt(sum(quadrado_beta))

    quadrado_beta = [np.square(sum(betas)) for betas in valores_primeira_hiper()[1]]
    beta_vec_ww0 = np.sqrt(sum(quadrado_beta))

    print(beta_vec_000)
    print(beta_vec_ww0)

    return beta_vec_000, beta_vec_ww0


## Mostra a polarizabilidade Média

#print('-' * 20 + ' Polarizabilidade Media Alfa (0; 0) ' + '-' * 20)
polariz_media1, polariz_media2 = polarizabilidade_media()
#print(polariz_media1)
#print('-' * 76)
#print()
#print('-' * 20 + ' Polarizabilidade Media Alfa (-w, w) ' + '-' * 20)
#print(polariz_media2)
#print('-' * 76)
#print()


## Mostra o valor de beta_vec
beta_vec = calcula_beta_vec(valores_primeira_hiper())


#bv = np.sqrt(sum([np.square(sum(val_beta)) for val_beta in valores_primeira_hiper()]))
#print(bv)
#for i in valores_primeira_hiper():
#    print(i)

#calcula_beta_vec(valores_primeira_hiper())


arquivo = open('resultados_calc_ONL.dat', 'w')
#print('{:>30}'.format('Alfa (0;0)'))
arquivo.write('{:>40} {:>15}\n\n'.format('Alfa(0; 0)', 'Alfa(-w, w)'))
arquivo.write('Polarizabilidade Média')
arquivo.write('{:18.7f} {:14.7f}\n'.format(polariz_media1, polariz_media2))
arquivo.write('--------------------------------------------------------------------------------------\n')
arquivo.write('{:>40} {:>20} {:>20}\n\n'.format('Beta(0;0,0)', 'Beta(-w,w,0)', 'Beta(-2w,w,0)'))
arquivo.write('Primeira Hiper Polariz.')
arquivo.write('{:18.7f} {:18.7f}\n'.format(beta_vec[0], beta_vec[1]))
arquivo.write('{:>15}\n'.format('Beta vec'))
arquivo.write('--------------------------------------------------------------------------------------\n')

#arquivo.close()
