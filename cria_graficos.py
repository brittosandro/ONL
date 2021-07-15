import matplotlib.pyplot as plt
import re

class CriaGraficos:

    def __init__(self, path, arquivo):
        self.path = path
        self.arquivo = arquivo
        self.gera_graficos()

    def gera_graficos(self):

        with open(self.path+self.arquivo) as f:
            arq = f.readlines()

        funcional = slice(0, 11)
        valores = slice(12, 23)
        funcionais = [dados[funcional].strip() for dados in arq]
        valores_funcionais = [float(dados[valores].strip()) for dados in arq]

        rotulo = re.sub('.txt', '', self.arquivo)

        fig, ax = plt.subplots(figsize=(8, 6))
        # Ajusta subplots.
        fig.subplots_adjust(
                             left = 0.145,
                             right = 0.90,    # {Define as distâncias entre os extremos}
                             bottom = 0.18,
                             top = 0.93,
                             hspace = 0.24,   # Organiza espaçoes entre os subplots
                             wspace = 0.23    # Organiza espaçoes entre os subplots
                           )

        fig1 = ax.plot(funcionais, valores_funcionais, '-o', markersize=8, color='#6666FF', linewidth=2, label=rotulo)
        fig.legend(loc='upper right', shadow=False, fontsize='large', bbox_to_anchor=(0.89, 0.93), frameon=False)
        plt.xticks(rotation=40)
        
        # Descritores dos eixos
        fig.text(
               0.5,                      # Ordena posição x
               0.04,                     # Ordena posição y
              'Funcionais',
               ha = 'center',
               va = 'center',
               fontsize = 'xx-large'
               )

        fig.text(
                 0.03,
                 0.5,
                 rotulo,
                 ha = 'center',
                 va = 'center',
                 fontsize = 'xx-large',
                 rotation = 'vertical'
               )

        plt.savefig(
                    self.path + rotulo + '.png',
                    dpi=300,
                    orientation = 'portrait',
                    transparent = True,
                    format='png'
                )
