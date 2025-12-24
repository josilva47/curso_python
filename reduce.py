#reduce() reduz um iterável a um único valor, aplicando uma função acumuladora passo a passo.

from functools import reduce

produtos = [
    {'nome': 'produto 5', 'preco': 10.00},
    {'nome': 'produto 1', 'preco': 22.32},
    {'nome': 'produto 3', 'preco': 10.11},
    {'nome': 'produto 2', 'preco': 105.87},
    {'nome': 'produto 4', 'preco': 69.90},
]

#SEM REDUCE
total = 0
for p in produtos:
    total += p['preco']

print(total)

#COM REDUCE
novos_produtos = reduce(lambda ac, p: ac + p['preco'], produtos, 0) #Funçao(2 args), Iteravel, Valor inicial

print(novos_produtos)