import numpy as np

#distância euclidiana:

s1 = np.array((168, 398, 451, 337, 186, 232, 262, 349, 189, 204, 220, 220, 207, 239, 259, 258, 242, 331, 251, 323, 106,
      1055, 170))
s2 = np.array((168, 400, 451, 300, 186, 200, 262, 349, 189, 204, 220, 220, 207, 239, 259, 258, 242, 331, 251, 180, 106,
      1055, 200))

subtracao = s1 - s2
quadrado = subtracao * subtracao
somatorio = np.sum(quadrado)

distancia = np.sqrt(somatorio)
print("Distância euclidiana:", distancia)

#ou utilizando o módulo de álgebra linear:

distancia2 = np.linalg.norm(s1 - s2)
print("Distância (módulo AL):", distancia2)

#série temporal com os valores médios entre s1 e s2

media = (s1+s2)/2

print("Série temporal com valores médios entre s1 e s2:\n", media)

#série temporal com os valores máximos de cada instante entre s1 e s2

max = np.maximum(s1, s2)

print("Série temporal com os valores máximos entre s1 e s2:\n", max)

#série temporal com os valores mínimos de cada instante entres1es2

min = np.minimum(s1, s2)

print("Série temporal com os valores mínimos entre s1 e s2:\n", min)


