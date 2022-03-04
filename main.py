"""

https://wiki.python.org.br/ExerciciosArquivos
Faça um programa que leia um arquivo texto contendo
uma lista de endereços IP e gere um outro arquivo,
contendo um relatório dos endereços IP válidos e inválidos.


"""
import re
# Abro os arquivos | Leio os dados e salvo | analiso os dados | escreve no arquivo final
with open('./enderecos.txt', 'r') as doc:
    lista_inicial = [d.strip() for d in doc]
    ips_validos = [is_valid_ip(ip) for ip in lista_inicial]
    print(ips_validos)
