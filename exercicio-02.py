import matplotlib.pyplot as plt

idade = [4, 9, 14, 19, 24, 29, 34, 39, 44, 49, 54, 59, 64, 69, 74, 79, 84, 89, 94, 99, 100]
pop_fem = [6779171, 7345231, 8441348, 8432004, 8614963, 8643419, 8026854, 7121915, 6688796, 6141338,
           5305407, 4373877, 3468085, 2616745, 2074264, 1472930, 998349, 508724, 211594, 66806, 16989]

x_pos = [x for x in range(len(idade))]

plt.figure(figsize=(10, 8))

plt.bar(x_pos, pop_fem, align='center',
        color='pink', linewidth=2, edgecolor='black')

plt.yticks([1000000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000, 8000000, 9000000],
           ["1 mi", "2 mi", "3 mi", "4 mi", "5 mi", "6 mi", "7 mi", "8 mi", "9 mi"])

plt.xticks(x_pos,
           ["0 a 4", "5 a 9", "10 a 14", "15 a 19", "20 a 24", "25 a 29", "30 a 34", "35 a 39", "40 a 44", "45 a 49",
            "50 a 55", "56 a 59", "60 a 64", "65 a 69", "70 a 74", "75 a 79", "80 a 84", "85 a 89", "90 a 94",
            "95 a 99", "100+"], rotation=90)

plt.title("Distribuição da população feminina por idade")

plt.xlabel("Idade (anos)")
plt.ylabel("População feminina")

plt.grid(b=True, color='gray', linestyle='--', linewidth=0.5);

plt.show()