"""
A funçao lambda é uma função como qualquer outra em Python. Porem,
são funções anônimas que contém apenas uma linha. ou seja, tudo
deve ser contido dentro de uma única expresão.
"""

lista = [
    {'nome': 'Luiz', 'sobrenome': 'Miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

def exibir(lista):
    for l in lista:
        print(l)

l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

exibir(l1)
print()
exibir(l2)

soma = lambda n1, n2: n1 + n2

print(soma(1, 2))