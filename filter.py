def print_iter(iterator):
    print(*iterator, sep='\n')
    print()

produtos = [
    {'nome': 'produto 5', 'preco': 10.00},
    {'nome': 'produto 1', 'preco': 22.32},
    {'nome': 'produto 3', 'preco': 10.11},
    {'nome': 'produto 2', 'preco': 105.87},
    {'nome': 'produto 4', 'preco': 69.90},
]

#SEM FILTER
novos_produtos = [
    p for p in produtos 
    if p['preco'] > 20
]

print_iter(novos_produtos)

#COM FILTER
novos_produtos_filter = filter(lambda p: p['preco'] > 20, produtos) #funçao, iteravel
print_iter(novos_produtos_filter)
