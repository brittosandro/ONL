from itertools import chain
from collections import defaultdict

arq = open("ONL_B0TMC_0_B3LYP.log", "r")
string_arq = arq.read()
arq.close()

separador1 = ' Electric dipole moment'
separador2 = ' Alpha(0;0):'
separador3 = ' Alpha(-w;w) w= 1898.5nm:'
separador4 = ' Beta(0;0,0):'
separador5 = ' Beta(-w;w,0) w= 1898.5nm:'
separador6 = ' Beta(-2w;w,w) w= 1898.5nm:'
separador7 = ' Gamma(0;0,0,0):'
separador8 = ' Gamma(-w;w,0,0) w= 1898.5nm:'
separador9 = ' Gamma(-2w;w,w,0) w= 1898.5nm:'
separador10 = ' ' + '-' * 70

comp_momento_de_dipolo = slice(2, 6)
valor_momento_de_dipolo = slice(30, 44)

comp_alfa_00 = slice(2, 8)
valor_alfa_00 = slice(31, 44)

comp_alfa_ww = slice(2, 8)
valor_alfa_ww = slice(31, 44)

comp_beta_000 = slice(2, 9)
valor_beta_000 = slice(30, 44)

comp_beta_ww0 = slice(2, 9)
valor_beta_ww0 = slice(30, 44)

comp_beta_2www = slice(2, 9)
valor_beta_2www = slice(30, 44)

comp_gama_0000 = slice(2, 7)
valor_gama_0000 = slice(30, 44)

comp_gama_ww00 = slice(2, 7)
valor_gama_ww00 = slice(30, 44)

comp_gama_2www0 = slice(2, 7)
valor_gama_2ww0 = slice(30, 44)


################################# Inicia a extração do momento de dipolo

momento_de_dipolo0 = {}
lista0 = string_arq.split(separador1)[1].split(separador2)[0].split('\n')[3:7]
for comp in lista0:
    momento_de_dipolo0[comp[comp_momento_de_dipolo].strip()] = comp[valor_momento_de_dipolo].strip().replace('D', 'e')

arq = open('momendo_de_dipolo_input_ori_0.dat', 'w')
for i, j in momento_de_dipolo0.items():
    arq.write('{:5s} {} \n'.format(i, j))
arq.close()
#print(momento_de_dipolo0)

momento_de_dipolo1 = {}
lista1 = string_arq.split(separador1)[2].split(separador2)[0].split('\n')[3:7]
for comp in lista1:
    momento_de_dipolo1[comp[comp_momento_de_dipolo].strip()] = comp[valor_momento_de_dipolo].strip().replace('D', 'e')

momento_de_dipolo2 = defaultdict(list)
for k, v in chain(momento_de_dipolo0.items(), momento_de_dipolo1.items()):
    momento_de_dipolo2[k].append(v)

#print(momento_de_dipolo2)

#print('-'*40)

#for k, v in momento_de_dipolo2.items():
#    print(k, v)

########## Termina aqui o momento de dipolo

''' Inicia extração de alfa(0;0) '''

#print('\n\n')

valores_alfa_00_0 = {}

lista0 =
for comp in lista0:
    #print(comp[comp_alfa_00])
    #print(comp[valor_alfa_00])
    valores_alfa_00_0[comp[comp_alfa_00].strip()] = comp[valor_alfa_00].strip().replace('D', 'e')

arq = open('alfa(0;0)_input_ori_0.dat', 'w')
for i, j in valores_alfa_00_0.items():
    arq.write('{:5s} {} \n'.format(i, j))
arq.close()

#print(valores_alfa_00_0)

#print()
#print(valores_alfa_00_0)
#print()

valores_alfa_00_1 = {}

lista1 = string_arq.split(separador2)[2].split(separador3)[0].split('\n')[2:10]
for comp in lista1:
    #print(comp[comp_alfa_00])
    #print(comp[valor_alfa_00])
    valores_alfa_00_1[comp[comp_alfa_00].strip()] = comp[valor_alfa_00].strip().replace('D', 'e')

valores_alfa_00_2 = defaultdict(list)
for k, v in chain(valores_alfa_00_0.items(), valores_alfa_00_1.items()):
    valores_alfa_00_2[k].append(v)

#print()
#print(valores_alfa_00_2)
#print()

#for k, v in valores_alfa_00_2.items():
#    print(k, v)

#print(lista1)

########################### Termina extração de alfa (0, 0) ########################################

''' Inicia extração de Alfa(-w, w) '''

valores_alfa_ww_0 = {}

lista0 = string_arq.split(separador3)[1].split(separador4)[0].split('\n')[2:10]
for comp in lista0:
    #print(comp[comp_alfa_ww])
    #print(comp[valor_alfa_ww])
    valores_alfa_ww_0[comp[comp_alfa_ww].strip()] = comp[valor_alfa_ww].replace('D', 'e').strip()

arq = open('alfa(-w,w)_input_ori_0.dat', 'w')
for i, j in valores_alfa_ww_0.items():
    arq.write('{:5s} {} \n'.format(i, j))
arq.close()
#print(valores_alfa_ww_0)

valores_alfa_ww_1 = {}
lista1 = string_arq.split(separador3)[2].split(separador4)[0].split('\n')[2:10]
for comp in lista1:
    #print(comp[comp_alfa_ww])
    #print(comp[valor_alfa_ww])
    valores_alfa_ww_1[comp[comp_alfa_ww].strip()] = comp[valor_alfa_ww].replace('D', 'e').strip()

#print(valores_alfa_ww_1)

valores_alfa_ww_2 = defaultdict(list)
for k, v in chain(valores_alfa_ww_0.items(), valores_alfa_ww_1.items()):
    valores_alfa_ww_2[k].append(v)


#print(lista1)
#print(valores_alfa_ww_2)

############################### Termina extração de alfa(-w, w) #######################

''' Extração de beta(0; 0, 0) '''

valores_beta_000_0 = {}

lista0 = string_arq.split(separador4)[1].split(separador5)[0].split('\n')[2:18]
for comp in lista0:
    #print(comp[comp_beta_000])
    #print(comp[valor_beta_000])
    valores_beta_000_0[comp[comp_beta_000].strip()] = comp[valor_beta_000].replace('D', 'e').strip()

arq = open('beta(0;0,0)_input_ori_0.dat', 'w')
for i, j in valores_beta_000_0.items():
    arq.write('{:7s} {} \n'.format(i, j))
arq.close()


#print(valores_beta_000_0)

valores_beta_000_1 = {}
lista1 = string_arq.split(separador4)[2].split(separador5)[0].split('\n')[2:18]
for comp in lista1:
    #print(comp[comp_beta_000])
    #print(comp[valor_beta_000])
    valores_beta_000_1[comp[comp_beta_000].strip()] = comp[valor_beta_000].replace('D', 'e').strip()

valores_beta_000_2 = defaultdict(list)
for k, v in chain(valores_beta_000_0.items(), valores_beta_000_1.items()):
    valores_beta_000_2[k].append(v)

#print(valores_beta_000_2)

################################### Termina extração de beta(0; 0, 0) ###############################

''' Começa extração de beta(-w, w, 0) '''

valores_beta_ww0_0 = {}
lista0 = string_arq.split(separador5)[1].split(separador6)[0].split('\n')[2:26]
for comp in lista0:
    valores_beta_ww0_0[comp[comp_beta_ww0].strip()] = comp[valor_beta_ww0].strip().replace('D', 'e')

arq = open('beta(-w;w,0)_input_ori_0.dat', 'w')
for i, j in valores_beta_ww0_0.items():
    arq.write('{:7s} {} \n'.format(i, j))
arq.close()

valores_beta_ww0_1 = {}
lista1 = string_arq.split(separador5)[2].split(separador6)[0].split('\n')[2:26]
for comp in lista1:
    valores_beta_ww0_1[comp[comp_beta_ww0].strip()] = comp[valor_beta_ww0].strip().replace('D', 'e')

valores_beta_ww0_2 = defaultdict(list)
for k, v in chain(valores_beta_ww0_0.items(), valores_beta_ww0_1.items()):
    valores_beta_ww0_2[k].append(v)

################################### Termina extração de beta(-w; w, 0) ###############################

''' Começa extração de beta(-2w, w, 0) '''

valores_beta_2www_0 = {}

lista0 = string_arq.split(separador6)[1].split(separador7)[0].split('\n')[2:26]
for comp in lista0:
    #print(comp[comp_beta_2www])
    #print(comp[valor_beta_2www])
    valores_beta_2www_0[comp[comp_beta_2www].strip()] = comp[valor_beta_2www].strip().replace('D', 'e')

arq = open('beta(-2w;w,0)_input_ori_0.dat', 'w')
for i, j in valores_beta_2www_0.items():
    arq.write('{:7s} {} \n'.format(i, j))
arq.close()

#print(valores_beta_2www_0)

valores_beta_2www_1 = {}
lista1 = string_arq.split(separador6)[2].split(separador7)[0].split('\n')[2:26]
for comp in lista1:
    #print(comp[comp_beta_2www])
    #print(comp[valor_beta_2www])
    valores_beta_2www_1[comp[comp_beta_2www].strip()] = comp[valor_beta_2www].strip().replace('D', 'e')

valores_beta_2www_2 = defaultdict(list)
for k, v in chain(valores_beta_2www_0.items(), valores_beta_2www_1.items()):
    valores_beta_2www_2[k].append(v)

#print(valores_beta_2www_2)

################################### Termina extração de beta(-2w; w, w) ###############################

''' Começa extração de gamma(0;0,0,0) '''

valores_gama_0000_0 = {}
lista0 = string_arq.split(separador7)[1].split(separador8)[0].split('\n')[2:19]
for comp in lista0:
    #print(comp[comp_gama_0000])
    #print(comp[valor_gama_0000])
    valores_gama_0000_0[comp[comp_gama_0000].strip()] = comp[valor_gama_0000].strip().replace('D', 'e')

arq = open('gama(0;0,0,0)_input_ori_0.dat', 'w')
for i, j in valores_gama_0000_0.items():
    arq.write('{:7s} {} \n'.format(i, j))
arq.close()

#print(valores_gama_0000_0)

valores_gama_0000_1 = {}
lista1 = string_arq.split(separador7)[2].split(separador8)[0].split('\n')[2:19]
for comp in lista1:
    #print(comp[comp_gama_0000])
    #print(comp[valor_gama_0000])
    valores_gama_0000_1[comp[comp_gama_0000].strip()] = comp[valor_gama_0000].strip().replace('D', 'e')

valores_gama_0000_2 = defaultdict(list)
for k, v in chain(valores_gama_0000_0.items(), valores_gama_0000_1.items()):
    valores_gama_0000_2[k].append(v)

#print(valores_gama_0000_2)

################################### Termina extração de gama(0; 0, 0, 0) ###############################

''' Começa extração de gamma(-w;w,0,0) '''

valores_gama_ww00_0 = {}
lista0 = string_arq.split(separador8)[1].split(separador9)[0].split('\n')[2:40]
for comp in lista0:
    #print(comp[comp_gama_ww00])
    #print(comp[valor_gama_ww00])
    valores_gama_ww00_0[comp[comp_gama_ww00].strip()] = comp[valor_gama_ww00].strip().replace('D', 'e')

arq = open('gama(-w;w,0,0)_input_ori_0.dat', 'w')
for i, j in valores_gama_ww00_0.items():
    arq.write('{:7s} {} \n'.format(i, j))
arq.close()

#print(valores_gama_ww00_0)

valores_gama_ww00_1 = {}
lista1 = string_arq.split(separador8)[2].split(separador9)[0].split('\n')[2:40]
for comp in lista1:
    #print(comp[comp_gama_ww00])
    #print(comp[valor_gama_ww00])
    valores_gama_ww00_1[comp[comp_gama_ww00].strip()] = comp[valor_gama_ww00].strip().replace('D', 'e')

valores_gama_ww00_2 = defaultdict(list)
for k, v in chain(valores_gama_ww00_0.items(), valores_gama_ww00_1.items()):
    valores_gama_ww00_2[k].append(v)

#print(valores_gama_ww00_2)

################################### Termina extração de gama(-w; w, 0, 0) ###############################

''' Começa extração de gamma(-2w;w,w,0) '''

valores_gama_2www0_0 = {}
lista0 = string_arq.split(separador9)[1].split(separador10)[0].split('\n')[2:-2]
for comp in lista0:
    #print(comp[comp_gama_2www0])
    #print(comp[valor_gama_2ww0])
    valores_gama_2www0_0[comp[comp_gama_2www0].strip()] = comp[valor_gama_2ww0].strip().replace('D', 'e')

arq = open('gama(2w;w,0,0)_input_ori_0.dat', 'w')
for i, j in valores_gama_2www0_0.items():
    arq.write('{:7s} {} \n'.format(i, j))
arq.close()

#print(valores_gama_2www0_0)

valores_gama_2www0_1 = {}
lista1 = string_arq.split(separador9)[2].split(separador10)[0].split('\n')[2:-2]
for comp in lista1:
    #print(comp[comp_gama_2www0])
    #print(comp[valor_gama_2ww0])
    valores_gama_2www0_1[comp[comp_gama_2www0].strip()] = comp[valor_gama_2ww0].strip().replace('D', 'e')

valores_gama_2www0_2 = defaultdict(list)
for k, v in chain(valores_gama_2www0_0.items(), valores_gama_2www0_1.items()):
    valores_gama_2www0_2[k].append(v)

#print(valores_gama_2www0_2)

'''
comp_momento_de_dipolo = slice(2, 6)
valor_momento_de_dipolo = slice(30, 44)


print(string_arq.split(tag1)[1].split(tag2)[0].split('\n')[3:6])

list_momento_dipolo = string_arq.split(tag1)[1].split(tag2)[0].split('\n')[3:7]

for componente in list_momento_dipolo:
    print(componente[comp_momento_de_dipolo].strip())
    print(componente[valor_momento_de_dipolo].strip())
'''
