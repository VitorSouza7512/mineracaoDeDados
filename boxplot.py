import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('dados.csv')

Atributo_D = df['Atributo_D']
Atributo_D_desc = Atributo_D.describe()

with open ('Atributo_D_descricao.txt', 'w') as f:
    Atributo_D_desc.to_string(f)
q1 = Atributo_D_desc['25%']     
mediana = Atributo_D_desc['50%']
q3 =  Atributo_D_desc['75%']

s_q1 = "{0:.2f}".format(q1)
s_mediana = "{0:.2f}".format(mediana)
s_q3 = "{0:.2f}".format(q3)


font_1 = {'family': 'serif', 'color': 'darkred', 'size':'14'}

plt.figure(figsize=(6, 7))
plt.boxplot(Atributo_D)
plt.title('Boxplot Atributo_D')
plt.ylabel('Atributo_D')
plt.text(1, q1, s_q1, fontdict=font_1)
plt.text(1, mediana, s_mediana, fontdict=font_1)
plt.text(1, q3, s_q3, fontdict=font_1)
plt.savefig('vitorsouza-boxplotD.png')
plt.close()
