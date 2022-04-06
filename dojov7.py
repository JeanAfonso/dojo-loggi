def pascal_triangle(profundidade):
    list_of_all = [[1]]
    for profundidade_da_linha in range(1, profundidade):
        lista_anterior = list_of_all[profundidade_da_linha - 1]
        lista_atual = []
        for indice in range(0, profundidade_da_linha + 1):
            if indice == 0 or indice == profundidade_da_linha:
                valor_atual = 1
            else:
                valor_atual = lista_anterior[indice] + lista_atual[indice - 1]

            lista_atual.append(valor_atual)
        print(lista_atual)
        list_of_all.append(lista_atual)
    return list_of_all

"""
[
[1],
[1,1],
[1,2,1],
[1,3,3,1],
[1,4,6,4,1],
]
"""

lista_final = pascal_triangle(5)
print(lista_final)
