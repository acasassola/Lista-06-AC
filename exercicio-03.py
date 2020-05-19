import matplotlib.pyplot as plt

idade = [4, 9, 14, 19, 24, 29, 34, 39, 44, 49, 54, 59, 64, 69, 74, 79, 84, 89, 94, 99, 100]
pop_masc = [7016987, 7624144, 8725413, 8558868, 8630229, 8460995, 7717658, 6766664, 6320568, 5692014, 4834995,
            3902344, 3041035, 2224065, 1667372, 1090517, 668623, 310759, 114964, 31529, 7247]

x_pos = [x for x in range(len(idade))]

plt.figure(figsize=(8, 10))

plt.barh(x_pos, pop_masc, align='center',
         color='blue', linewidth=2, edgecolor='black')

plt.xticks([1000000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000, 8000000, 9000000],
           ["1 mi", "2 mi", "3 mi", "4 mi", "5 mi", "6 mi", "7 mi", "8 mi", "9 mi"])

plt.yticks(x_pos,
           ["0 a 4", "5 a 9", "10 a 14", "15 a 19", "20 a 24", "25 a 29", "30 a 34", "35 a 39", "40 a 44", "45 a 49",
            "50 a 55", "56 a 59", "60 a 64", "65 a 69", "70 a 74", "75 a 79", "80 a 84", "85 a 89", "90 a 94",
            "95 a 99", "100+"])

plt.title("Distribuição da população masculina por idade")

plt.xlabel("População masculina")
plt.ylabel("Idade (anos)")

plt.grid(b=True, color='gray', linestyle='--', linewidth=0.5);

plt.show()