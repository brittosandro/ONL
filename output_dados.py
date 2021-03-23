class CriaTabela:

    def __init__(self, *valores):
        self.cria_tabela(valores)

    def cria_tabela(self, valores):
        #nome_tabela = input('Informe o nome da Tabela: ')
        nome_tabela = valores[0].replace('ONL_', '').replace('log', 'dat')
        arq = open(nome_tabela, 'w')

        if valores[1] == 1:
            arq.write('  ############################################################\n')
            arq.write('  #                                                          #\n')
            arq.write('  #        Esses são os dados da molécula Isolada            #\n')
            arq.write('  #                                                          #\n')
            arq.write('  ############################################################\n\n\n')
        else:
            arq.write('############################################################\n')
            arq.write('#                                                          #\n')
            arq.write('#   Esses são os dados da molécula Cristal                 #\n')
            arq.write('#                                                          #\n')
            arq.write('############################################################\n\n\n')


        arq.write('{} {:>55}\n'.format('Processo', 'Polarizabilidade Média <alfa> 10**-24 esu'))
        arq.write('-' * 70 + '\n')
        arq.write('{:>5} {:26.7f}\n'.format('Alfa(0;0)', float(valores[2])))
        arq.write('-' * 70 + '\n')
        arq.write('{:>5} {:25.7f}\n'.format('Alfa(-w;w)', float(valores[3])))
        arq.write('-' * 70 + '\n\n')

        arq.write('{} {:>47}\n'.format('Processo', 'Primeira Hiper  Total 10**-30 esu'))
        arq.write('-' * 70 + '\n')
        arq.write('{:>5} {:25.7f}\n'.format('Beta(0;0,0)', float(valores[4])))
        arq.write('-' * 70 + '\n')
        arq.write('{:>5} {:25.7f}\n'.format('Beta(-2w;w,w)', float(valores[8])))
        arq.write('-' * 70 + '\n\n')

        arq.write('{} {:>47}\n'.format('Processo', 'Primeira Hiper  b_vec 10**-30 esu'))
        arq.write('-' * 70 + '\n')
        arq.write('{:>5} {:25.7f}\n'.format('Beta(0;0,0)', float(valores[5])))
        arq.write('-' * 70 + '\n')
        arq.write('{:>5} {:25.7f}\n'.format('Beta(-2w;w,w)', float(valores[9])))
        arq.write('-' * 70 + '\n\n')

        arq.write('{} {:>52}\n'.format('Processo', 'Primeira Hiper  mi_beta_vec 10**-48 esu'))
        arq.write('-' * 70 + '\n')
        arq.write('{:>5} {:25.7f}\n'.format('Beta(0;0,0)', float(valores[6])))
        arq.write('-' * 70 + '\n')
        arq.write('{:>5} {:25.7f}\n'.format('Beta(-2w;w,w)', float(valores[10])))
        arq.write('-' * 70 + '\n\n')

        arq.write('{} {:>59}\n'.format('Processo', 'Primeira Hiper  beta_vec_T_||_(z) 10**-30 esu'))
        arq.write('-' * 70 + '\n')
        arq.write('{:>5} {:25.7f}\n'.format('Beta(0;0,0)', float(valores[7])))
        arq.write('-' * 70 + '\n')
        arq.write('{:>5} {:25.7f}\n'.format('Beta(-2w;w,w)', float(valores[11])))
        arq.write('-' * 70 + '\n\n')

        arq.write('{} {:>51}\n'.format('Processo', 'Segunda Hiper  gama_medio 10**-36 esu'))
        arq.write('-' * 70 + '\n')
        arq.write('{:>5} {:25.7f}\n'.format('gama(0;0,0,0)', float(valores[12])))
        arq.write('-' * 70 + '\n')
        arq.write('{:>5} {:25.7f}\n'.format('gama(-w;w,0,0)', float(valores[13])))
        arq.write('-' * 70 + '\n')
        arq.write('{:>5} {:25.7f}\n'.format('gama(-2w;w,w,0)', float(valores[14])))
        arq.write('-' * 70 + '\n\n')

        arq.write('{} {:>51}\n'.format('Processo', 'Segunda Hiper  Z SCAN 10**-36 esu'))
        arq.write('-' * 70 + '\n')
        arq.write('{:>5} {:25.7f}\n'.format('gama(-w;w,0,0)', float(valores[15])))
        arq.write('-' * 70 + '\n\n')

        #arq.write('{} {:>43}\n'.format('Const. Dieletrica', 'Alfa estatico 10**-40 C**2 m**2 J**-1'))
        #arq.write('-' * 70 + '\n')
        #arq.write('{:>5} {:25.7f}\n'.format('EPSILON', float(valores[16])))
        #arq.write('-' * 70 + '\n')

        arq.close()
