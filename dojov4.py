# Exercise 3
# Write a program that, given an array v of n numbers and another number k,
# determines whether or not there exist two elements in v whose sum is exactly k.
# For example, given v = [10, 5, 2, 7] and k = 17, the output expected is true
# because (10 + 7 = 17).
# v = [10, 5, 2, 7]
# k = 21
#

def testearray(v, k): # N²
    for i in range(len(v) - 1):  # N -> acesso sequencial
        for j in range(i + 1, len(v)):  # N
            soma = v[i] + v[j]
            if soma == k:
                return True
    return False



# acesso sequencial: N
# acesso aleatorio: LOG(N)
# acesso direto: 1

def testearray2(v, k): # 2(N * LOG(N)) => N * LOG(N)
    v.sort() # N * log(n)
    for i in range(len(v) - 1):  # N -> acesso sequencial
        vj = k - v[i]
        j = pesquisa_binaria(v, vj) #LOG(N) -> acesso aleatorio
        if j >= 0 and j < len(v):
            return True
    return False

def testearray3(v, k): # => N
    d = {}
    for i in range(len(v)):  # N -> acesso sequencial
        d[v[i]] = i

    for i in range(len(v) - 1): # N -> acesso sequencial
        vj = k - v[i]
        if d.get(vj): # 1 -> Acesso direto
            return True
    return False

def pesquisa_binaria(v, valor):
    inicio = 0
    fim = len(v) - 1

    while inicio <= fim:
        meio = int((fim + inicio) / 2)

        if valor == v[meio]:
            return meio
        elif valor > v[meio]:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1


# print(pesquisa_binaria([ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ], 8))

#                        |
#                        V
# [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
#                  |
#                  V
#                   [ 7, 8, 9, 10 ]
#                           |
#                           V
#                   [ 7, 8 ]
#                        |
#                        V
