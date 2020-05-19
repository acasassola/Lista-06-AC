import matplotlib.pyplot as plt
import numpy as np

grupos = 6
valor_im = [13.1, 13.6, 14.2, 14, 13.8, 3.6]
valor_ex = [88.2, 84.9, 96, 101.2, 96.9, 21.4]
fig, ax = plt.subplots()
indice = np.arange(grupos)
bar_larg = 0.4
plt.bar(indice, valor_im, bar_larg, color='red', label='Importações')
plt.bar(indice + bar_larg, valor_ex, bar_larg, color='blue', label='Exportações')

plt.xticks(indice + 0.2, ('2015', '2016', '2017', '2018', '2019', '2020'))
plt.yticks([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
plt.xlabel('Ano')
plt.ylabel('US$ Bilhão')
plt.title('Balança comercial do Agronegócio no Brasil')
plt.legend()
plt.grid(b=True, color='gray', linestyle='--', linewidth=0.5)
plt.show()
