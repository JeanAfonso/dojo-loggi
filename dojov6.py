"""
Dado duas listas, encontre uma sublista com a interseção das duas primeiras.

Lista de entregador
Lista de recebedor
"""

listaA=[1,2,3,4,5,6]
listaB=[7,8,2,5,9,10]

def check_cpf(listaA, listaB):

    dicionario = {a: True for a in listaA } # dict comprehens

    print(dicionario)

    for b in listaB:
        if b in dicionario.keys():
            print(b)

print(check_cpf(listaA, listaB))


