# Dado um conjunto de N números inteiros representando o tamanho de luvas,
# faça um programa para contar o máximo possível de pares de luvas existentes no conjunto.
# Observe que uma luva só pode ser par de outra luva do mesmo tamanho e só pode fazer parte de um único par.
# Exemplo: entrada = {6, 5, 2, 3, 5, 2, 2, 1}, saída = 2 pares (tamanho 5 e tamanho 2).
import random


entrada = [6, 5, -1, 3, 5, -1, -1, 1]
contador = 1
contadorPares = 0

# [-1, -1, -1, 1, 3, 5, 5, 6]

entrada.sort()

for i in range(len(entrada) - 1):
    print(f"iteracao {i}")
    if entrada[i] == entrada[i+1]:
        print(f"{[i]} {entrada[i]} + {entrada[i+1]}")
        contador += 1
    else:
        contadorPares += int(contador/2)
        contador = 1

# contadorPares += 1



# for e in range(len(entrada)):
#     for i in range(e + 1, len(entrada)):
#         if entrada[i] == entrada[e] and auxiliar[e] != -1:
#                 auxiliar[e] = -1
#                 auxiliar[i] = -1
#                 contadorPares += 1

print(f"{contadorPares} pares encontrados!")
print(entrada)






