import matplotlib.pyplot as plt
import numpy as np

idades = ["0 a 4 anos", "5 a 9 anos", "10 a 14 anos", "15 a 19 anos", "20 a 24 anos", "25 a 29 anos", "30 a 34 anos",
         "35 a 39 anos", "40 a 44 anos", "45 a 49 anos", "50 a 54 anos", "55 a 59 anos", "60 a 64 anos", "65 a 69 anos",
         "70 a 74 anos", "75 a 79 anos", "80 a 84 anos", "85 a 89 anos", "90 a 94 anos", "95 a 99 anos", "100 anos e mais"]

pop_masc = [7016987, 7624144, 8725413, 8558868, 8630229, 8460995, 7717658, 6766664, 6320568, 5692014, 4834995,
             3902344, 3041035, 2224065, 1667372, 1090517, 668623, 310759, 114964, 31529, 7247]

pop_fem = [6779171, 7345231, 8441348, 8432004, 8614963, 8643419, 8026854, 7121915, 6688796, 6141338, 5305407, 4373877,
            3468085, 2616745, 2074264, 1472930, 998349, 508724, 211594, 66806, 16989]

x_pos = np.arange(21)

plt.figure(figsize=(12,8))

pop_masc_array = np.array(pop_masc)
pop_fem_array = np.array(pop_fem)

plt.barh(x_pos, -pop_masc_array, label='Masculino', color='blue')
plt.barh(x_pos, pop_fem_array, label='Feminino', color='pink')

plt.title("Distribuição da População por sexo segundo os grupos de idade – Brasil – 2010")
plt.ylabel("Idades")
plt.xlabel("População")

plt.yticks(x_pos, idades, rotation=0)
plt.xticks(
    [-9000000,-8000000,-7000000,-6000000,-5000000,-4000000,-3000000,-2000000,-1000000,0,1000000,2000000,3000000,
     4000000,5000000,6000000,7000000,8000000,9000000],
    ["9 mi","8 mi","7 mi","6 mi","5 mi","4 mi","3 mi","2 mi","1 mi","0","1 mi","2 mi","3 mi","4 mi","5 mi","6 mi",
     "7 mi","8 mi","9 mi"])

plt.grid(b=True, color='gray', linestyle='--', linewidth=0.3)

plt.legend(loc='best')

plt.show()