# ONL 

- Este repositório apresenta como finalidade extrair dados de arquivos *.log provenientes do Gaussian 
e calcular alguns processos ONL.

- Os principais processos calculados são:

 1) Polarizabilidade Média <alfa> 10**-24 esu
     Alfa estático Alfa(0;0)
     Alfa dinânico Alfa(-w;w) 

 2) Primeira Hiperpolarizabilidade Total 10**-30 esu
     Beta estático Beta(0;0,0)
     Beta dinâmico Beta(-2w;w,w)

 3) Primeira Hiper  b_vec 10**-30 esu
     Beta estático Beta(0;0,0)
     Beta dinâmico Beta(-2w;w,w)
   
 4) Primeira Hiper  mi_beta_vec 10**-48 esu
     Beta estático Beta(0;0,0)
     Beta dinâmico Beta(-2w;w,w)

 5) Primeira Hiper  beta_vec_T_||_(z) 10**-30 esu
     Beta estático Beta(0;0,0)
     Beta dinâmico Beta(-2w;w,w)
  
 6) Segunda Hiper  gama_medio 10**-36 esu
     gama(0;0,0,0)
     gama(-w;w,0,0)  
     gama(-2w;w,w,0)

 7) Segunda Hiper  Z SCAN 10**-36 esu
     gama(-w;w,0,0) 

- Para usar esses scripts basta executar o arquivo processa.py.

- Após executar o arquivo processa.py será gerado um novo diretório chamado de Resultados com arquivos *.dat e alguns gráficos. 
